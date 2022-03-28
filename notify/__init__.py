import poshpy
import sys

wincmd = """
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")

$objNotifyIcon = New-Object System.Windows.Forms.NotifyIcon

$objNotifyIcon.Icon = [System.Drawing.SystemIcons]::{icon}
$objNotifyIcon.BalloonTipIcon = "{largeicon}"
$objNotifyIcon.BalloonTipText = "{title}"
$objNotifyIcon.BalloonTipTitle = "{content}"
$objNotifyIcon.Visible = ${vis}

$objNotifyIcon.ShowBalloonTip({time})

"""

def psh(cmd):
    completed_cmd = poshpy.execute_command(cmd)
    if completed_cmd.return_code == 0:
        return (completed_cmd.standard_out)
    else:
        return (completed_cmd.standard_error)

def notify(icon="Information",largeicon="Info",title="",content="",Visible="True",time="1000"):
    w = wincmd
    w = w.replace("{icon}",icon).replace("{largeicon}",largeicon).replace("{title}",title).replace("{content}",content).replace("{vis}",Visible).replace("{time}",time)
    if sys.platform.startswith("win"):
        psh(w)
    else:
        raise RuntimeError("Currently only supported for windows")
