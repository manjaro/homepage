New Manjaro Homepage
======================

![Alt text](/preview/manjaro-nhp.png?raw=true)

Source code of our new launch page for Manjaro Linux

## How to preview this on your local PC

* Install **hugo** on Manjaro with `yaourt -S hugo`
* clone this repository to your local pc with `https://github.com/manjaro/homepage.git`
* change in the new dir with `cd homepage`
* do a test run with `hugo server`
* preview the homepage with any webbrowser from `http://localhost:1313/`

## How to preview this current version

* simply click on [here](https://manjaro.github.io/homepage/public/)

## How to develop this homepage further

* read the [Beginners Guide of Hugo](https://gohugo.io/overview/quickstart/) first
* modify the theme in [partials](https://github.com/manjaro/homepage/tree/gh-pages/themes/hugo-creative-theme/layouts/partials) and [static](https://github.com/manjaro/homepage/tree/gh-pages/themes/hugo-creative-theme/static) if needed
* edit the [config file](https://github.com/manjaro/homepage/blob/gh-pages/config.toml) to your needs
* run a preview on your local machine with `hugo server` from your **localhost**
* when satisfied run `hugo` to render the pages
* check **baseurl** in **public** and [change](https://github.com/manjaro/homepage/commit/8e3334067af2c5d40dc04eb402cf8100556b7fb3) if needed
* tell us about your fork
