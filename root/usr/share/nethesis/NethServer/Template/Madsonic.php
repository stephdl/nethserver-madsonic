<?php

/* @var $view Nethgui\Renderer\Xhtml */

echo $view->header()->setAttribute('template', $T('Madsonic_header'));

echo $view->panel()

    ->insert($view->fieldsetSwitch('status', 'enabled',$view::FIELDSETSWITCH_CHECKBOX | $view::FIELDSETSWITCH_EXPANDABLE)->setAttribute('uncheckedValue', 'disabled')

->insert($view->radioButton('access', 'green'))
->insert($view->radioButton('access', 'red'))
//->insert($view->textInput('TCPPort'))

->insert($view->textArea('SambaUsers', $view::LABEL_ABOVE)->setAttribute('dimensions', '5x30')->setAttribute('placeholder', $view['Users_default']))

);

echo $view->buttonList($view::BUTTON_SUBMIT); # | $view::BUTTON_HELP);

