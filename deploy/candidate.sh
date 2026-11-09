#!/usr/bin/env bash
# Run from the host as its normal development user, after validating/pushing dev.
set -euo pipefail
cd "$(dirname "$0")/.."
[[ $(git branch --show-current) == dev ]] || { echo 'Use the dev branch.' >&2; exit 1; }
[[ -z $(git status --porcelain) ]] || { echo 'Commit validated changes to dev first.' >&2; exit 1; }
git fetch origin dev
release_commit=$(git rev-parse HEAD)
[[ $release_commit == "$(git rev-parse origin/dev)" ]] || { echo 'Publish this dev commit first.' >&2; exit 1; }
prod_env=${GLPI_PROD_ENV_FILE:-$HOME/.config/glpi-arbos/prod.env}
[[ -f $prod_env ]] || { echo "Missing private environment file: $prod_env" >&2; exit 1; }
docker_cmd=(docker)
if ! docker info >/dev/null 2>&1; then docker_cmd=(sudo docker); fi
release_image="glpi-arbos:$release_commit"
export GLPI_PROD_IMAGE="$release_image"
if [[ ${docker_cmd[0]} == sudo ]]; then docker_cmd=(sudo --preserve-env=GLPI_PROD_IMAGE docker); fi
"${docker_cmd[@]}" build --build-arg "GLPI_COMMIT=$release_commit" -f deploy/Dockerfile.prod -t "$release_image" .
# Named volumes preserve Prod data; application source is bundled in the image.
GLPI_PROD_IMAGE="$release_image" "${docker_cmd[@]}" compose --env-file "$prod_env" -f deploy/compose.prod.yaml up -d --wait
printf 'Prod candidate: %s\nValidate http://localhost:8081 before promoting main.\n' "$release_commit"
