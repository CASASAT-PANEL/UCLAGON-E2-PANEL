from Plugins.Plugin import PluginDescriptor
from Components.ActionMap import ActionMap
from Screens.Screen import Screen
from Components.MenuList import MenuList
from Components.Label import Label
from Screens.MessageBox import MessageBox
import urllib.request
import os
import zipfile
import subprocess


class Plugin(Screen):
    skin = """
        <screen name="Plugin" position="center,center" size="600,600" title="PANEL" titleFont="Action_Force.ttf; 30" > <!-- Modifiez la taille de la police ici -->
            <widget name="menu" position="80,60" size="400,400" itemHeight="40" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- RECEIVERS', 'receivers'), ('2- CHANNELS', 'channels'), ('3- PLUGINS', 'plugins'),('4- PICONS', 'picons'), ('5- SOFTCAMS', 'softcams'), ('6- IPTV', 'IPTV'), ('7- TOOLS', 'TOOLS'), ('8- UPDATE', 'UPDATE'), ('9- ABOUT', 'ABOUT') ] # Add other options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'ok': self.onSelection,
            'cancel': self.close,
        }, -2)

    def onSelection(self):
        current_item = self.menu.getCurrent()[1]
        if current_item == 'receivers':
            self.session.open(ReceiversScreen)
        elif current_item == 'channels':
            self.session.open(ChannelsScreen)
        elif current_item == 'plugins':
            self.session.open(PluginsScreen)
        elif current_item == 'picons':
            self.session.open(PiconsScreen)
        elif current_item == 'softcams':
            self.session.open(SoftcamsScreen)
        elif current_item == 'IPTV':
            self.session.open(IPTVScreen)
        elif current_item == 'TOOLS':
            self.session.open(ToolsScreen)
        elif current_item == 'UPDATE':
            if check_for_updates():
                download_and_install_update()
            else:
                self.session.open(MessageBox, "No update available.", type=MessageBox.TYPE_INFO)
        elif current_item == 'ABOUT':
            self.session.open(ABOUTScreen)


class ReceiversScreen(Screen):
    skin = """
        <screen name="ReceiversScreen" position="center,center" size="600,600" title="RECEIVERS E2">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- DREAMBOX', 'dreambox'), ('2- VUPLUS', 'Vuplus'), ('3- OCTAGON_8008', 'Octagon'), ('4- UCLAN_PRO', 'Uclan')] # Add other options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
            'ok': self.onSelection,
        }, -2)

    def onSelection(self):
        current_item = self.menu.getCurrent()[1]
        if current_item == 'dreambox':
            self.session.open(DreamboxScreen)
        elif current_item == 'Vuplus':
            self.session.open(VuplusScreen)
        elif current_item == 'Octagon':
            self.session.open(OctagonScreen)
        elif current_item == 'Uclan':
            self.session.open(UclanScreen)

class DreamboxScreen(Screen):
    skin = """
        <screen name="DreamboxScreen" position="center,center" size="600,600" title="DREAMBOX">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- DREAMBOX 900', 'DM900'), ('2- DREAMBOX 920', 'DM920'), ('3- DREAM ONE', 'DMONE'), ('4- DREAM TWO', 'DMTWO')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
            'ok': self.onSelection,
        }, -2)

    def onSelection(self):
        current_item = self.menu.getCurrent()[1]
        if current_item == 'DM900':
            # Ouvrir DMImagesScreen
            self.session.open(DM900ImagesScreen)
        elif current_item == 'DM920':
            # Ouvrir une autre classe d'écran pour DM920 si nécessaire
            self.session.open(DM920ImagesScreen)
        elif current_item == 'DMONE':
            # Ouvrir une autre classe d'écran pour Dream ONE si nécessaire
            self.session.open(DMONEImagesScreen)
        elif current_item == 'DMTWO':
            # Ouvrir une autre classe d'écran pour Dream TWO si nécessaire
            self.session.open(DMTWOImagesScreen)

 
class DM900ImagesScreen(Screen):
    skin = """
        <screen name="DM900ImagesScreen" position="center,center" size="600,600" title="DM900 IMAGES">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- GEMINI_4.2', 'gemini_4.2'), ('2- DREAMELITE', 'dreamelite'), ('3- MERLIN', 'merlin'), ('4- OPENATV', 'openatv'), ('5- OPENPLI', 'openpli'), ('6- EGAMI', 'egami'), ('7- OPENSPA', 'openspa')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)

class DM920ImagesScreen(Screen):
    skin = """
        <screen name="DM920ImagesScreen" position="center,center" size="600,600" title="DM920 IMAGES">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- GEMINI_4.2', 'gemini_4.2'), ('2- DREAMELITE', 'dreamelite'), ('3- MERLIN', 'merlin'), ('4- OPENATV', 'openatv'), ('5- OPENPLI', 'openpli'), ('6- EGAMI', 'egami'), ('7- OPENSPA', 'openspa')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)

class DMONEImagesScreen(Screen):
    skin = """
        <screen name="DMONEImagesScreen" position="center,center" size="600,600" title="DMONE IMAGES">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- GEMINI_4.2', 'gemini_4.2'), ('2- DREAMELITE', 'dreamelite'), ('3- MERLIN', 'merlin'), ('4- OPENATV', 'openatv'), ('5- OPENPLI', 'openpli'), ('6- EGAMI', 'egami'), ('7- OPENSPA', 'openspa')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)

class DMTWOImagesScreen(Screen):
    skin = """
        <screen name="DMTWOImagesScreen" position="center,center" size="600,600" title="DMTWO IMAGES">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- GEMINI_4.2', 'gemini_4.2'), ('2- DREAMELITE', 'dreamelite'), ('3- MERLIN', 'merlin'), ('4- OPENATV', 'openatv'), ('5- OPENPLI', 'openpli'), ('6- EGAMI', 'egami'), ('7- OPENSPA', 'openspa')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)


class VuplusScreen(Screen):
    skin = """
        <screen name="VuplusScreen" position="center,center" size="600,600" title="Vuplus">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- Zero 4k', 'zero'), ('2- Uno 4k se', 'uno'), ('3- Dual 4k se', 'dual'), ('4- Ultimo', 'ultimo')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
            'ok': self.onSelection,
        }, -2)

    def onSelection(self):
        current_item = self.menu.getCurrent()[1]
        if current_item == 'zero':
            # Ouvrir DMImagesScreen
            self.session.open(ZeroImagesScreen)
        elif current_item == 'uno':
            # Ouvrir une autre classe d'écran pour uno si nécessaire
            self.session.open(unoImagesScreen)
        elif current_item == 'dual':
            # Ouvrir une autre classe d'écran pour dual si nécessaire
            self.session.open(dualImagesScreen)
        elif current_item == 'ultimo':
            # Ouvrir une autre classe d'écran pour ultimo si nécessaire
            self.session.open(ultimoImagesScreen)

class ZeroImagesScreen(Screen):
    skin = """
        <screen name="zeroImagesScreen" position="center,center" size="600,600" title="ZERO 4K IMAGES">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- VTI', 'vti'), ('2- BLACKHOLE', 'blackhole'), ('3- OPENBLACKHOLE', 'openblackhole'), ('4- OPENATV', 'openatv'), ('5- OPENPLI', 'openpli'), ('6- EGAMI', 'egami'), ('7- OPENSPA', 'openspa')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)

class unoImagesScreen(Screen):
    skin = """
        <screen name="unoImagesScreen" position="center,center" size="600,600" title="UNO 4K SE IMAGES">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- VTI', 'vti'), ('2- BLACKHOLE', 'blackhole'), ('3- OPENBLACKHOLE', 'openblackhole'), ('4- OPENATV', 'openatv'), ('5- OPENPLI', 'openpli'), ('6- EGAMI', 'egami'), ('7- OPENSPA', 'openspa')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)       

class dualImagesScreen(Screen):
    skin = """
        <screen name="dualImagesScreen" position="center,center" size="600,600" title="DUAL 4K SE IMAGES">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- VTI', 'vti'), ('2- BLACKHOLE', 'blackhole'), ('3- OPENBLACKHOLE', 'openblackhole'), ('4- OPENATV', 'openatv'), ('5- OPENPLI', 'openpli'), ('6- EGAMI', 'egami'), ('7- OPENSPA', 'openspa')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)  

class ultimoImagesScreen(Screen):
    skin = """
        <screen name="ultimoImagesScreen" position="center,center" size="600,600" title="ULTIMO 4K SE IMAGES">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- VTI', 'vti'), ('2- BLACKHOLE', 'blackhole'), ('3- OPENBLACKHOLE', 'openblackhole'), ('4- OPENATV', 'openatv'), ('5- OPENPLI', 'openpli'), ('6- EGAMI', 'egami'), ('7- OPENSPA', 'openspa')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)  

class OctagonScreen(Screen):
    skin = """
        <screen name="OctagonScreen" position="center,center" size="600,600" title="OCTAGON 8008">
            <widget name="menu" position="80,60" size="400,400" itemHeight="30" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- DEFINE_OS', 'define_os'), ('2- OpenATV', 'openatv'), ('3- OpenPLI', 'openpli'), ('4- OpenSPA', 'openspa'), ('5- OpenBlackhole', 'openblackhole'), ('6- Egami', 'Egami'), ('7- OpenVision', 'Openvision'), ('8- OpenVIX', 'Openvix'), ('9- OpenDroid', 'Opendroid'), ('10- Pure2', 'Pure2'), ('11- CobraLiberosat', 'Cobraliberosat'), ('12- NonSoloSat', 'NonSolosat')]
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'ok': self.onSelection,
            'cancel': self.close,
        }, -2)

    def onSelection(self):
        current_item = self.menu.getCurrent()[1]
        print("Current item:", current_item)  # Ajoutez cette ligne pour déboguer
        if current_item == 'define_os':
            # URL de téléchargement de l'archive Define_os
            download_url = "http://define-sw.dyndns.tv/octagon/sf8008/octagon_sf8008-v1.06.47_20240329_mmc.zip"
            # Chemin de destination pour sauvegarder l'archive
            save_path = "/media/hdd/images/"
            # Nom du fichier téléchargé
            file_name = os.path.join(save_path, "octagon_sf8008-v1.06.47_20240329_mmc.zip")

            try:
                # Téléchargement de l'archive Define_os
                urllib.request.urlretrieve(download_url, file_name)
                # Extraire le contenu de l'archive
                #with zipfile.ZipFile(file_name, 'r') as zip_ref:
                   # zip_ref.extractall(save_path)
                # Supprimer l'archive ZIP après extraction
                #os.remove(file_name)
                self.session.open(MessageBox, "L'image Define_os a été téléchargée avec succès et sauvegardée dans /media/hdd/images.", type=MessageBox.TYPE_INFO)
            except Exception as e:
                # Gérer les erreurs de téléchargement ou d'extraction
                self.session.open(MessageBox, f"Erreur lors du téléchargement et de la sauvegarde de l'image Define_os : {str(e)}", type=MessageBox.TYPE_ERROR)
        elif current_item == 'openatv':
            # Exécuter la commande wget pour télécharger et installer OpenATV
            try:
                subprocess.call(['wget', 'https://dreambox4u.com/emilnabil237/images/openatv-7.4.sh', '-O', '-', '|', '/bin/sh'])
                self.session.open(MessageBox, "OpenATV installed successfully!", type=MessageBox.TYPE_INFO)
            except Exception as e:
                print("Error installing OpenATV:", e)
                self.session.open(MessageBox, "Error installing OpenATV.", type=MessageBox.TYPE_ERROR)
        else:
            self.session.open(MessageBox, "Invalid selection.", type=MessageBox.TYPE_ERROR)


class UclanScreen(Screen):
    skin = """
        <screen name="UclanScreen" position="center,center" size="600,600" title="UCLAN_PRO">
            <widget name="menu" position="80,60" size="400,400" itemHeight="30" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- DENYS_OS', 'denys_os'), ('2- OpenATV', 'openatv'), ('3- OpenPLI', 'openpli'), ('4- OpenSPA', 'openspa'), ('5- OpenBlackhole', 'openblackhole'), ('6- Egami', 'Egami'), ('7- OpenVision', 'Openvision'), ('8- OpenVIX', 'Openvix'), ('9- OpenDroid', 'Opendroid'), ('10- Pure2', 'Pure2'), ('11- CobraLiberosat', 'Cobraliberosat'), ('12- NonSoloSat', 'NonSolosat')] # Add other Denys options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)


class ChannelsScreen(Screen):
    skin = """
        <screen name="ChannelsScreen" position="center,center" size="600,600" title="CHANNELS">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />

        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- Vhannibal_Astra 19,2º', 'vhannibal_astra'), ('2- Vhannibal_Hotbird 13º', 'vhannibal_hotbird'), ('3- Vhannibal_Dual', 'vhannibal_dual'), ('4- Vhannibal_Motor', 'vhannibal_motor')] # Add other channel options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)


class PluginsScreen(Screen):
    skin = """
        <screen name="PluginsScreen" position="center,center" size="600,600" title="PLUGINS">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />

        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- MultiStalker', 'MultiStalker'), ('2- MultiStalkerPro', 'MultiStalkerPro'), ('3- IPAudioPro', 'IPAudioPro'), ('4- BouquetMakerXtream', 'BouquetMakerXtream')] # Add other plugin options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)


class PiconsScreen(Screen):
    skin = """
        <screen name="PiconsScreen" position="center,center" size="600,600" title="PICONS">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />

        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- ASTRA 19.2º_PICON', 'Astra 19.2º_PICON'), ('2- HOTBIRD 13º_PICON', 'Hotbird 13º_PICON'), ('3- DUAL_PICON', 'dual_PICON'), ('4- Motor_PICON', 'motor_PICON')] # Add other picons options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)


class SoftcamsScreen(Screen):
    skin = """
        <screen name="SoftcamsScreen" position="center,center" size="600,600" title="SOFTCAMS">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />

        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- CCCAM', 'cccam'), ('2- OSCAM', 'oscam'), ('3- NCAM', 'ncam'), ('4- MiCAM', 'micam'), ('5- NCAMICAM', 'ncamicam'), ('6- OSCAMICAM', 'oscamicam'), ('7- POWERCAM', 'powercam')] # Add other softcams options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)


class IPTVScreen(Screen):
    skin = """
        <screen name="IPTVScreen" position="center,center" size="600,600" title="IPTV">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />

        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- M3U', 'm3u'), ('3- STALKER', 'STALKER'), ('4- XTREAM', 'xtream')] # Add other IPTV options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)


class ToolsScreen(Screen):
    skin = """
        <screen name="ToolsScreen" position="center,center" size="600,600" title="TOOLS">
            <widget name="menu" position="80,60" size="400,400" itemHeight="50" />

        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('1- Barry_Allen', 'Barry_Allen'), ('2- Newboot', 'Newboot'), ('3- Alan Turing', ' Alan Turing')] # Add other tools options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)


class ABOUTScreen(Screen):
    skin = """
        <screen name="ABOUTScreen" position="center,center" size="600,600" title="ABOUT">
            <widget name="menu" position="60,80" size="400,400" itemHeight="50" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [('          Plugin for Enigma2 receivers', 'by TEAM'), ('            By Team: KARIM & SAID', 'bySaid')] # Add other plugin options as needed
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['actions'] = ActionMap(['OkCancelActions'], {
            'cancel': self.close,
        }, -2)


def check_for_updates():
    # Ajoutez ici le code pour vérifier les mises à jour disponibles
    return True  # Simuler une mise à jour disponible

def download_and_install_update():
    # Ajoutez ici le code pour télécharger et installer la mise à jour
    pass  # Placeholder pour la démonstration


def main(session, **kwargs):
    session.open(Plugin)

def Plugins(**kwargs):
    return [PluginDescriptor(
        name="UCLAGON E2 PANEL",
        description="Plugin for Enigma2 receivers By KARIM & SAID",
        icon="icon.png",
        where=[PluginDescriptor.WHERE_PLUGINMENU],
        fnc=main,
    )]