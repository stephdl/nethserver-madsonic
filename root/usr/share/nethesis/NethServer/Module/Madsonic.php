<?php
namespace NethServer\Module;


use Nethgui\System\PlatformInterface as Validate;

/**
 * Control Madsonic music streamer
 * 
 * @author stephane de Labrusse <stephdl@de-labrusse.fr>
 */
class Madsonic extends \Nethgui\Controller\AbstractController
{

    protected function initializeAttributes(\Nethgui\Module\ModuleAttributesInterface $base)
    {
        return \Nethgui\Module\SimpleModuleAttributesProvider::extendModuleAttributes($base, 'Configuration', 6);
    }

    public function initialize()
    {
        parent::initialize();
        $this->declareParameter('status', Validate::SERVICESTATUS, array('configuration', 'madsonic', 'status'));
        $this->declareParameter('SambaUsers', Validate::ANYTHING, array('configuration', 'madsonic', 'SambaUsers'));
        $this->declareParameter('access', $this->createValidator()->memberOf('green','red'), array('configuration', 'madsonic', 'access'));
    }


    public static function splitLines($text)
    {
        return array_filter(preg_split("/[,;\s]+/", $text));
    }
    public function readSambaUsers($dbList)
    {
        return implode("\r\n", explode(',' ,$dbList));
    }
    public function writeSambaUsers($viewText)
    {
        return array(implode(',', self::splitLines($viewText)));
    }

    public function validate(\Nethgui\Controller\ValidationReportInterface $report)
    {
        parent::validate($report);
        $itemValidator = $this->getPlatform()->createValidator(\Nethgui\System\PlatformInterface::USERNAME);
        foreach (self::splitLines($this->parameters['SambaUsers']) as $v) {
            if ( ! $itemValidator->evaluate($v)) {
                $report->addValidationErrorMessage($this, 'SambaUsers', 'Must be a user name', array($v));
                break;
            }
        }
    }


    protected function onParametersSaved($changedParameters)
    {
        parent::onParametersSaved($changedParameters);
        $this->getPlatform()->signalEvent('nethserver-madsonic-update');
    }

}

