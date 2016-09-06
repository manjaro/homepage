+++
date = "2016-09-05T21:03:22+02:00"
title = "First steps"
type = "support-post"
weight = 0
right = false
navsection = "support"
+++

Here are some first steps after you [downloaded](;baseurl;download) Manjaro. This guide covers only the basic steps, so if you want more information look into the [Manjaro User Guide](;baseurl;support/userguide/) or the [Manjaro Wiki](https://wiki.manjaro.org/).

So you downloaded Manjaro as an ISO file. An ISO file contains all files Manjaro needs to start an installation compressed into a handy file, which you can then use to make a [DVD](https://wiki.manjaro.org/index.php?title=Burn_an_ISO_File) or [USB-Stick](https://wiki.manjaro.org/index.php?title=Burn_an_ISO_File#Writing_to_a_USB_Stick_in_Linux) that can be run by your computer. This file can be directly used by a virtual machine if yout don't want to try out Manjaro on your actual computer, yet.

## Branching Paths
---

To try out Manjaro, you can either directly load it from a DVD or USB-Drive or use a  [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) if you are unsure or want to be able to use your current operating-system without [dual-booting](https://en.wikipedia.org/wiki/Multi-booting). Here you can find a list of all options you have and their pros and cons.

|   |   |
|---|---|
| ![Icon](;baseurl;/img/try/virtual-machine.svg) | **Using a virtual machine** |
|                                                | ➕ Leaves your current system untouched |
|                                                | ➕ Experiment without breaking something |
|                                                | ➕ Work parallel with Manjaro and your current system |
|                                                | ➖ Manjaro runs slower due to emulation |
|                                                | ➖ Emulation needs many system resources |
|                                                | |
|                                                | **[Find out how this works](#using-a-virtual-machine)** |
|   |   |
| ![Icon](;baseurl;/img/try/live-boot.svg) | **Only using the live-system**[¹](#glossary) |
|                                                | ➕ Leaves your current system untouched unless you modify it manually |
|                                                | ➕ Experiment without breaking something |
|                                                | ➕ All settings are stored on the medium - take it everywhere you want (USB-Drive only) |
|                                                | ➖ Manjaro runs slower due to slower speed of DVD or USB |
|                                                | |
|                                                | **[Find out how this works](#making-a-live-system)** |
|   |   |
| ![Icon](;baseurl;/img/try/install.svg) | **Install Manjaro** |
|                                                | ➕ Maximum performance and support |
|                                                | ➕ Install it alongside your current system if you want |
|                                                | ➖ You need to prepare (e.g. backup your data) as with every installation of an operating system|
|                                                | |
|                                                | **[Find out how this works](#install-manjaro)** |

![Pipeline](;baseurl;/img/support/firststeps-overview.png)

## Using a virtual machine
---
A virtual machine is a computer that runs "in" your current computer. If you just want to try or use Manjaro without rebooting your computer, you can set up a virtual machine. We will give you a quick step-by-step guide, but if you want to know more, visit our [Wiki](https://wiki.manjaro.org/index.php?title=VirtualBox#Running_Manjaro_in_VirtualBox).

|   |   |
|---|---|
| ![Icon](;baseurl;/img/actions/download.svg) | **1. Download an application that allows creating virtual machines and install it** |
|                                             | You can use for example [VirtualBox](https://www.virtualbox.org/), [VmWare Player](http://www.vmware.com/) or other software |
| ![Icon](;baseurl;/img/actions/vm.svg) | **2. Create a virtual machine** |
|                                             | ... for "Arch Linux" if Manjaro is not available as option |                                              
|                                             | ... with at least 20-30GB virtual harddrive space |                                              
|                                             | ... with at least 2GB RAM/Memory |                                              
|                                             | **Also don't forget to** |                                              
|                                             | ... give the machine at least 2 CPU cores |     
|                                             | ... increase the graphics memory |     
|                                             | ... enable 3D acceleration if possible | 
| ![Icon](;baseurl;/img/try/install.svg) | **3. Load Manjaro** |
|                                             | • Start the virtual machine and select the Manjaro ISO to be loaded into the virtual DVD drive | 
|                                             | • Manjaro will now boot. Select Manjaro (Free drivers) or leave it until it's automatically selected |
|                                             | • Manjaro now boots into the live environment |
| ![Icon](;baseurl;/img/features/installation.svg) | **4. Install Manjaro into the virtual machine** |
|                                             | **[Find out how this works](#install-manjaro)** |
| ![Icon](;baseurl;/img/actions/settings.svg) | **5. Finish the process** |
|                                             | • Go into the settings of the virtual machine and unload the Manjaro ISO |
|   |   |

Now you can just start your virtual computer with Manjaro, play around with it and use software that is not well supported on other operating systems! Note that this is (while being virtual) an actual computer, so you have to shut down Manjaro just like all operating systems. If you want to know what you can do after installing Manjaro, give a look at our [user guide](;baseurl;support/userguide/) and our [wiki](https://wiki.manjaro.org/index.php?title=Main_Page#Customisation_and_Configuration).


## Making a Live-System
---

To be able to install or try Manjaro on your computer, you need to put it on a DVD or USB-Drive. Then the computer will start (or "boot") from this medium into Manjaro's live-system[¹](#glossary).

### Create a bootable USB-Stick
|   |   |
|---|---|
| ![Icon](;baseurl;/img/actions/download.svg) | **1. Download an application that is able to create a bootable USB-Drive** |
|                                             | You can use for example [ImageWriter](https://launchpad.net/win32-image-writer/), [Rufus](https://rufus.akeo.ie/) or other software. See our [wiki](https://wiki.manjaro.org/index.php?title=Burn_an_ISO_File) for more information.  |
| ![Icon](;baseurl;/img/try/live-boot.svg)     | **2. Select the ISO and the stick and put Manjaro onto it** |
|                                             | Please don't forget to backup the data of your stick before doing this. |
|                                             | If you need more information, just visit our [Wiki](https://wiki.manjaro.org/index.php?title=Burn_an_ISO_File) |
| ![Icon](;baseurl;/img/actions/boot.svg)     | **3. Boot from USB** |
|                                             | **[Find out how this works](#booting-into-the-live-environment)**   |


### Burn a DVD
|   |   |
|---|---|
| ![Icon](;baseurl;/img/actions/download.svg) | **1. Download an application that is able to burn a disk** |
|                                             | You can use for example [DeepBurner](http://www.deepburner.com/), or if available the software that comes with your operating system |
| ![Icon](;baseurl;/img/actions/burn.svg)     | **2. Burn the Manjaro ISO to the DVD** |
|                                             | If you need more information, just visit our [Wiki](https://wiki.manjaro.org/index.php?title=Burn_an_ISO_File) |
| ![Icon](;baseurl;/img/actions/boot.svg)     | **3. Boot from DVD** |
|                                             | **[Find out how this works](#booting-into-the-live-environment)**   |

### Booting into the Live-System
|   |   |
|---|---|
| ![Icon](;baseurl;/img/actions/boot.svg)     | **1. Boot from USB or DVD** |
|                                             | If you are lucky, just have to plug-in the drive or put the DVD into the tray and restart your computer. |
|                                             | But sometimes you need to configure your system to allow this.  Then you may find help here:|
|                                             | • [How to Boot Your Computer From a Disc or USB Drive](http://www.howtogeek.com/129815/beginner-geek-how-to-change-the-boot-order-in-your-computers-bios/)
|                                             | • [BIOS and UEFI - Manjaro Wiki](https://wiki.manjaro.org/index.php?title=BIOS_and_UEFI) |
|                                             | • [Manjaro User Guide](;baseurl;support/userguide/)   |
| ![Icon](;baseurl;/img/actions/settings.svg)     | **2. Choose the drivers** |
|                                             | If you boot into the live-system, you can choose between "free" and "proprietary" drivers. |
|                                             | • Choose "proprietary" if you use a Nvidia graphics card or need wireless  |
|                                             | • Choose "free" if you are using a virtual machine or know that everything will work without proprietary drivers  |
|                                             | If you want more information, take a look at our [user guide](;baseurl;support/userguide/).   |

Now you have booted into Manjaro's live-environment and can begin to play around with it or proceed to install Manjaro on your computer (or the virtual machine). In the next section, you can find a quick step-by-step guide how to install Manjaro.

## Install Manjaro
---
There are many different ways to install Manjaro and the process depends heavily from your current hardware. If you want more detailed steps, you will find them in our [user guide](;baseurl;support/userguide/). Here we will give you a rough outline how to install Manjaro.

|   |   |
|---|---|
| ![Icon](;baseurl;/img/actions/install.svg)  | **1. Start the installer** |
|                                             | If you boot into the live-system, there's a welcome-window that has an option "Install" or "Installation using Calamares". Click on this option to start the installer. |
|                                             | If you closed the welcome-window, you can find it in the application menu as "Manjaro Welcome". |
| ![Icon](;baseurl;/img/actions/settings.svg)  | **2. Put in your data** |
|                                             | Insert your timezone, preferred keyboard layout and language. |
| ![Icon](;baseurl;/img/actions/partition.svg)  | **3. Determine where Manjaro should be installed** |
|                                             | If you use a virtual machine or want to wipe your whole system (keep in mind that if you use a virtual machine, you only wipe the machine, not your actual computer) choose "erase disk". |
|                                             | Otherwise the installer offers plenty of options such as installing Manjaro alongside your current operating system. Experienced users also can partition manually. |
|                                             | We recommend to take a look at the [user guide](;baseurl;support/userguide/) and our [wiki](https://wiki.manjaro.org/index.php?title=BIOS_and_UEFI) to make sure that nothing goes wrong. Also we recommend to make backups of your important data before installing Manjaro. You can do this directly in the live-environment if you forgot it.   |
| ![Icon](;baseurl;/img/try/install.svg)  | **4. Finish the installation** |
|                                             | • Insert your account data and wait until the installation is finished. You can use the live-environment while doing an installation to maybe watch some videos or browsing the web.|
|                                             | • Restart your machine |

Congratulations! You have now installed Manjaro. If there are any problems, you can maybe find a solution [here](;baseurl;support/commonproblems), our [user guide](;baseurl;support/userguide/) or our [wiki](https://wiki.manjaro.org/). Our [user guide](;baseurl;support/userguide/) also contains information how to use Manjaro. Also we recommend to visit our [forums](https://forum.manjaro.org/) where people discuss about problems, new programs and make customizations like wallpapers.

## Glossary
|   |   |
|---|---|
| **Live-Environment / Live-System**  | Manjaro and many other Linux distributions allow running the system directly from a USB-Drive or DVD.<br/>Those "Live-Enviroments" are completely functional systems and can be used as portable operating-system or to rescue data if something went wrong.  |