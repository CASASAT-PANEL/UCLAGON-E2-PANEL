
echo "################ UCLAGON-E2-PANEL #################"
echo "############ KARIM&SAID #################"
#!/bin/sh
#

wget -O /usr/lib/enigma2/python/Plugins/Extensions/UCLAGON-E2-PANEL "https://raw.githubusercontent.com/CASASAT-PANEL/UCLAGON-E2-PANEL/main/__init__.py"

wget -O /usr/lib/enigma2/python/Plugins/Extensions/UCLAGON-E2-PANEL "https://github.com/CASASAT-PANEL/UCLAGON-E2-PANEL/raw/main/__init__.pyc"

wget -O /usr/lib/enigma2/python/Plugins/Extensions/UCLAGON-E2-PANEL "https://raw.githubusercontent.com/CASASAT-PANEL/UCLAGON-E2-PANEL/main/plugin.py"

wget -O /usr/lib/enigma2/python/Plugins/Extensions/UCLAGON-E2-PANEL "https://github.com/CASASAT-PANEL/UCLAGON-E2-PANEL/raw/main/plugin.pyc"

wget -O /usr/lib/enigma2/python/Plugins/Extensions/UCLAGON-E2-PANEL "https://github.com/CASASAT-PANEL/UCLAGON-E2-PANEL/raw/main/plugin.pyc"

wget -O /usr/lib/enigma2/python/Plugins/Extensions/UCLAGON-E2-PANEL "https://files.catbox.moe/j4pto1.png"


echo ""
cd ..
sync
echo "############ INSTALLATION COMPLETED ########"
echo "############ RESTARTING... #################" 
init 4
sleep 2
init 3
exit 0
