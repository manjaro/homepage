+++
Name = ""
type="problem-post"
category="after_installation"
title = "Updating fails"
+++

|   |   |
|---|---|
| ![Icon](;baseurl;/img/actions/question.svg) | **Check if you are connected with the internet** |
|   |   |
| ![Icon](;baseurl;/img/actions/warning.svg) | **Maybe the current mirror is not reachable** |
|                                                   | Open a [terminal](;baseurl;commonproblems/howtoterminal) and enter: |
|                                                   | `sudo pacman-mirrors -g` |
|                                                   | More information about this in our [wiki](https://wiki.manjaro.org/index.php?title=Manjaro_Mirrors) |
|   |   |
| ![Icon](;baseurl;/img/actions/warning.svg) | **Maybe the cache is full** |
|                                                   | Some editions come with a cache cleaner. Just search `cache` in the application menu. |
|                                                   | If no cache cleaner is available, open a [terminal](;baseurl;commonproblems/howtoterminal) and enter: |
|                                                   | `sudo pacman -Scc` |
|                                                   | More information about this in our [wiki](https://wiki.manjaro.org/index.php?title=Pacman_Tips#Cleaning_Packages) |
|   |   |