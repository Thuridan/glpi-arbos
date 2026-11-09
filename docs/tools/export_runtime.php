<?php
require '/var/www/glpi/vendor/autoload.php';
$kernel = new Glpi\Kernel\Kernel();
$kernel->boot();
$out = ['version' => GLPI_VERSION, 'api_version' => Glpi\Api\HL\Router::API_VERSION, 'api' => [], 'web' => []];
foreach (Glpi\Api\HL\Router::getInstance()->getAllRoutes() as $r) {
    $m = $r->getMethod();
    $out['api'][] = ['path'=>$r->getRoutePath(), 'methods'=>$r->getRouteMethods(), 'security'=>$r->getRouteSecurityLevel(), 'scopes'=>$r->getRouteScopes(), 'version'=>(array)$r->getRouteVersion(), 'controller'=>$r->getController(), 'method'=>$m->getName(), 'source'=>str_replace('/var/www/glpi/', '', $m->getFileName()), 'line'=>$m->getStartLine()];
}
foreach ($kernel->getContainer()->get('router')->getRouteCollection() as $name => $r) {
    $controller=$r->getDefault('_controller');
    $out['web'][]=['name'=>$name,'path'=>$r->getPath(),'methods'=>$r->getMethods(),'controller'=>is_string($controller)?$controller:get_debug_type($controller)];
}
usort($out['api'],fn($a,$b)=>[$a['path'],$a['methods']]<=>[$b['path'],$b['methods']]);
usort($out['web'],fn($a,$b)=>$a['path']<=>$b['path']);
if (!isset($RELATION)) { require '/var/www/glpi/inc/relation.constant.php'; }
$out['relations']=$RELATION;
echo json_encode($out, JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE).PHP_EOL;
