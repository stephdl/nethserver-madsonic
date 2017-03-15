<?php
namespace NethServer\Module\Dashboard\Applications;
/**
 * madsonic web interface
 *
 * @author stephane de labrusse
 */
class Madsonic extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "Madsonic Music Streamer";
    }

    public function getInfo()
    {
         $port = $this->getPlatform()->getDatabase('configuration')->getProp('madsonic','TCPPort');
         $host = explode(':',$_SERVER['HTTP_HOST']);
         return array(
            'url' => "https://".$host[0].":$port",
         );
    }
}
