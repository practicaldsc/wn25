---
layout: page
title: 🕸️ Website Instructions
description: Instructions for creating a website for your Final Project.
nav_order: 2
parent: 📊 Final Project
---

# {{ page.title }}
{:.no_toc}

See below for instructions on how to create your website in Part 2. Make sure you've read the [main project specifications](../) first.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Content

Your website must clearly contain the following five headings, corresponding to the five steps mentioned in [Part 1](../#part-1-analysis) of the main spec:

- Introduction
- Data Cleaning and Exploratory Data Analysis
- Framing a Prediction Problem
- Baseline Model
- Final Model

**Don't** include "Step 1", "Step 2", etc. in your headings – the headings should be exactly as they are above.

The specific content your website needs to contain is described in the "Report on Website" columns above. **Make sure to also give your website a creative title that relates to the question you're trying to answer, and clearly state your name(s) and email(s).**

---

## Initializing a GitHub Pages Site

As mentioned in the main spec, the easiest (and free) option is to use GitHub Pages with Jekyll. If you'd like to follow the official [GitHub Pages and Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll) tutorial, you're welcome to, though we will provide you with a perhaps simpler set of instructions here.

A very basic site with an embedded visualization can be found at [rampure.org/dsc80-proj3-test1/](http://rampure.org/dsc80-proj3-test1/); the source code for the site is [here](https://github.com/surajrampure/dsc80-proj3-test1). Note that this example site doesn't have the same headings that you're required to have.

### Step 1: Initializing a Jekyll GitHub Pages Site

1. Create a GitHub account, if you don't already have one.
1. Create a new GitHub repository for your project. Give it a descriptive name, like `league-of-legends-analysis`, not `eecs398-final-project`.
   - GitHub Pages sites live at `<username>.github.io/<reponame>` (for instance, the site for [github.com/practicaldsc.org/fa24](https://github.com/practicaldsc/fa24) is [practicaldsc.github.io/fa24](https://practicaldsc.github.io/fa24), which we redirect to from [practicaldsc.org/fa24](https://practicaldsc.org/fa24)).
   - As such, **don't** include "EECS 398" or "Final Project" in your repo's name – this looks unprofessional to future employers, and gives you a generic-sounding URL. Instead, mention that this is a project for EECS 398 at U-M in the repository description.
   - **Make sure to make your repository public.**
   - Select "ADD a README file." This ensures that your repository starts off non-empty, which is necessary to continue.
1. Click "Settings" in the repository toolbar (next to "Insights"), then click "Pages" in the left menu.
1. Under "Branch", click the "None" dropdown, change the branch to "main", and then click "Save." You should soon see "GitHub Pages source saved." in a blue banner at the top of the page. This initiates GitHub Pages in your repository.
1. After 30 seconds, reload the page again. You should see "**Your site is live at http://username.github.io/reponame/**". Click that link – you now have a site!
1. Click "Code" in the repo toolbar to return to the source code for your repo.

Note that the source code for your site lives in `README.md`. **As you push changes to `README.md`, they will update on your site automatically within a few minutes!** Before moving forward, make sure that you can make basic edits:

1. Clone your repo locally.
1. Make some edits to `README.md`.
1. Push those changes back to GitHub, using the following steps:
   - Add your changes to "staging" using `git add README.md` (repeat this for any other files you add).
   - Commit your changes using `git commit -m '<some message here>'`, e.g. `git commit -m 'changed title of website'`.
   - Push your changes using `git push`.

Moving forward, we recommend making edits to your website source code locally, rather than directly on GitHub. This is in part due to the fact that you'll be creating folders and adding files to your source code.

### Step 2: Choosing a Theme

The default "theme" of a Jekyll site is not all that interesting.

To change the theme of your site:

1. Create a file in your repository called `_config.yml`.
1. Go [here](https://pages.github.com/themes/), and click the links of various themes until you find one you like.
1. Open the linked repository for the theme you'd like to use and scroll down to the "Usage" section of the README. Copy the necessary information from the README to your `_config.yml` and push it to your site.

For instance, if I wanted to use the Merlot theme, I'd put the following in my `_config.yml`:

```yml
remote_theme: pages-themes/merlot@v0.2.0
plugins:
  - jekyll-remote-theme # add this line to the plugins list if you already have one
```

Note that you're free to use any Jekyll theme, not just the ones that appear [here](https://pages.github.com/themes/). You are required to choose _some_ theme other than the default, though. See more details about themes [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll).

### Step 3: Embedding Content

Now comes the interesting part – actually including content in your site. The [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/) contains tips on how to format text and other page components in Markdown (and if you'd benefit by seeing an example, you could always look at the Markdown source of [this very page](https://raw.githubusercontent.com/practicaldsc/practicaldsc.github.io/refs/heads/main/final-project/website.md) – meta!).

Guides on how to embed specific pieces of content are in the next section.

---

## Visualizations and Tables

### Embedding Interactive Plotly Visualizations

What will be a bit tricky is embedding `plotly` plots in your site so that they are interactive. Note that you are **required** to do this, you cannot simply take screenshots of plots from your notebooks and embed them in your site. Here's how to embed a `plotly` plot directly in your site.

1. **Export the Plot to HTML:**
   First, you'll need to convert your plot to HTML. If `fig` is a `plotly` `Figure` object (for instance, the result of calling `px.express`, `go.Figure`, or `.plot` when `pd.options.plotting.backend = "plotly"` has been run), then the method `fig.write_html` saves the plot as HTML to a file. Call it using `fig.write_html('file-name.html', include_plotlyjs='cdn')`.
   - Change `'file-name.html'` to the path where you'd like to initially save your plot.
   - `include_plotlyjs='cdn'` tells `write_html` to load the source code for the `plotly` library from a server, rather than including the entire source code in your HTML file. This drastically reduces the size of the resulting HTML file, keeping your repo size down.
1. **Move the HTML File:**
   Move the `.html` file(s) you've created into a folder in your website repo called `assets` (or something similar).
   - Depending on where your template notebook is saved, you could combine this step with the step above by calling `fig.write_html` with the correct path (e.g. `fig.write_html('../league-match-analysis/assets/matches-per-year.html')`).
1. **Embed the Plot in Markdown:**
   In `README.md`, embed your plot using the following syntax:

    ```html
    <iframe
    src="assets/file-name.html"
    width="800"
    height="600"
    frameborder="0"
    ></iframe>
    ```

    - `iframe` stands for "inline frame"; it allows us to embed HTML files within other HTML files.
    - You can change the `width` and `height` arguments, but don't change the `frameBorder` argument.

Refer [here](https://rampure.org/dsc80-proj3-test1/#assessment-of-missingness) for a working example (and [here](https://github.com/surajrampure/dsc80-proj3-test1) for its source code).

{: .note }
Try your best to make your plots look professional and unique to your group – add axis labels, change the font and colors, add annotations, etc. Remember, potential employers will see this – you don't want your plots to look like everyone else's! If you'd like to match the styles of the `plotly` plots used in lecture (e.g. with the white backgrounds), you can import and use the `lec_utils.py` file that's in the `final-project` folder of our public repo, alongside `template.ipynb`.

### Embedding Tables

To convert a DataFrame in your notebook to Markdown source code (which you need to do for both the **Data Cleaning** and **Interesting Aggregates** sections of Step 2: Data Cleaning and Exploratory Data Analysis in Part 1), use the `.to_markdown()` method on the DataFrame. 
  
For instance, if you run a line like this in your **notebook**:

```py
print(counts[['semester', 'Count']].head().to_markdown(index=False))
```

The output will be something that looks like:

```
| semester    | Count |
|-------------|-------|
| Fall 2020   | 3     |
| Winter 2021 | 2     |
| Spring 2021 | 6     |
| Summer 2021 | 4     |
| Fall 2021   | 55    |
```

The output above contains a Markdown representation of the first 5 rows of `counts`, including only the `'semester'` and `'Count'` columns (and not including the index). **To put this on your website, copy the table-looking output above and paste it in your `README.md`, making sure there's at least one empty line before and after it.**

You can see how this appears [here](http://rampure.org/dsc80-proj3-test1/#assessment-of-missingness); remember, no screenshots (and also remember that the "Assessment of Missingness" title is not something you need to have, that's just an example website). You may need to play with this a little bit so that you don't show DataFrames that are super, super wide and look ugly.

For larger or more complex tables, you can export them as an HTML file. To export a DataFrame as `html`, use the `.to_html()` method on it. This will give you a string representation of the DataFrame as HTML, which you can then copy and save into some `.html` file which you load into your site as an `<iframe>`:

```html
# Here, table.html is an HTML file that you created by manually copying-and-pasting the output of df.to_html().
<iframe src="assets/table.html" width="800" height="400" frameborder="0">
</iframe>
```

### Site Organization

We'll stress that you should keep all images, HTML files, and other assets in a dedicated folder (e.g., `assets`) within your repository. This practice helps maintain a clean project structure and makes it much easier to update or locate files later.

---

## Local Rendering

The above instructions give you all you need to create and make updates to your site. However, you _may_ want to set up Jekyll locally, so that you can look at how changes to your site would look without having to push and wait for GitHub to re-build your site. To do so, follow the steps [here](https://jekyllrb.com/docs/installation/) and then [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll). The steps below largely come from these two sites.

### Step 1: Installation (Windows)

Using RubyInstaller for Windows:

1. **Install Ruby and Devkit:**
   - Download a Ruby+Devkit version (RubyInstaller-2.4 or newer) from the [RubyInstaller Downloads](https://rubyinstaller.org/downloads/). If you're not sure which version to choose, use the Ruby+Devkit 3.3.X (x64) installer—the bolded option starting with **=>**.
   - Use the default installation options.
   - In the final step of the installer, run the `ridk install` command and choose the "MSYS2 and MINGW development toolchain" option. This is necessary for building native extensions when installing gems.
1. **Set Up Your Environment:**
   - Open a new Command Prompt window (this ensures your udpated PATH is active).
1. **Install Jekyll and Bundler:**
   - Run the following command to install Jekyll and Bundler:
   ```bash
   gem install jekyll bundler
   ```
   - Verify the installation with:
   ```bash
   jekyll -v
   ```
   - If an error occurs, reboot your system and try again.
   - If you want to use Windows Subsystem for Linux (WSL), please consult [Installation via Bash on Windows 10](https://jekyllrb.com/docs/installation/windows/#installation-via-bash-on-windows-10).

### Step 1: Installation (macOS)

1. **Install Homebrew:**
   - Open Terminal and run:
   ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
1. **Install a Ruby Version Manager:**
   - Install **chruby** and **ruby-install** using Homebrew:
   ```bash
     brew install chruby ruby-install
   ```
1. **Install a Newer Ruby Version:**
   - Install the latest stable version of Ruby (e.g., 3.4.1) with:
     ```bash
     ruby-install ruby 3.4.1
     ```
   - Configure your shell to always use the correct version of Ruby. Run each of these lines, one by one, in your Terminal:
     ```bash
     echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
     echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
     echo "chruby ruby-3.4.1" >> ~/.zshrc
     ```
     **Important**: If you’re using Bash, replace `~/.zshrc` with `~/.bash_profile`. If you’re not sure, read this external guide to [find out which shell you’re using](https://www.moncefbelyamani.com/which-shell-am-i-using-how-can-i-switch/).
   - Quit and relaunch Terminal, then verify by running:
     ```bash
     ruby -v
     ```
     It should display Ruby 3.4.1 (or a newer version).
1. **Install Jekyll and Bundler:**
   - With the new Ruby version active, run:
     ```bash
     gem install jekyll bundler
     ```

### Step 2: Building Your Site Locally

These steps are largely taken from [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll#building-your-site-locally).

1. **Open your Terminal**.
1. **Navigate to Your Site's Publishing source:**
   - `cd` into your root folder where your Jekyll files (including `_config.yml`) are located.
1. **Install Dependencies with Bundler:**
   - Make sure you have a `Gemfile` in your site's root directory that lists all required gems (like Jekyll and any plugins). This should be there by default if you've cloned your site repo from GitHub.
   - Run the following command to install all dependencies:
   ```
   bundle install
   ```
   - This command reads your `Gemfile` and installs the necessary Ruby gems.
1. **Serve Your Jekyll Site Locally:**
   - To build your site and start a local web server, run:
   ```
   bundle exec jekyll serve
   ```
   - This command performs several tasks:
     - Reads your `_config.yml` file.
     - Builds your site into the `_site` directory.
     - Starts a local server (usually at `http://127.0.0.1:4000/`) with auto-regeneration enabled, so your site rebuilds when you make changes.
   - Open your web browser and go to `http://localhost:4000` to preview your site.
   - Moving forward, all you need to do is `cd` to your site repo and run `bundle exec jekyll serve` to preview your site.


If, after running the above steps, running `bundle exec jekyll serve` in your local website repository doesn't work, then follow these steps.
1. In your Terminal, `cd` to your local website repository (folder).
1. Run `bundle init` to create a Gemfile (a file that specifies which Ruby extensions your project needs).
1. Open the Gemfile created in your local repository, delete everything that's currently there, and replace it all with:

    ```
    source "https://rubygems.org"
    gem "github-pages", group: :jekyll_plugins
    ```

1. Run `bundle install` and then `bundle exec jekyll serve`.
1. If, after that, you still can't render your site locally, let us know what error `bundle exec jekyll serve` throws for you and we'll try and troubleshoot! Or, check out Jekyll's [Troubleshooting](https://jekyllrb.com/docs/troubleshooting/) page to see if your questions have already been answered.