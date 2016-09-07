+++
Name = ""
type="problem-post"
category="after_installation"
title = "Laptop screen is too dark"
+++

|   |   |
|---|---|
| ![Icon](;baseurl;/img/actions/information.svg) | **This is likely caused by your hardware manufacturer** |
|                                                   | More information about this in our [wiki](https://wiki.manjaro.org/index.php?title=Reactivating_the_Backlight) |
|   |   |
| ![Icon](;baseurl;/img/actions/execute.svg) | **Re-activate the backlight** |
|                                                   | Open a [terminal](;baseurl;commonproblems/howtoterminal) and enter: |
|                                                   | `sudo sed "s/\(GRUB_CMDLINE_LINUX=\)\"\"/\1\"acpi_osi=Linux acpi_backlight=vendor\"/" /etc/default/grub -i; sudo update-grub` |

