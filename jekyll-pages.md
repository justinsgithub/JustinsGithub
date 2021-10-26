# CheatSheet

## Setting Up Jekyll and GitHub Pages

- Installation
Jekyll is a Ruby Gem that can be installed on most systems.

RequirementsPermalink
Ruby version 2.5.0 or higher, including all development headers (check your Ruby version using ruby -v)
RubyGems (check your Gems version using gem -v)
GCC and Make (check versions using gcc -v,g++ -v, and make -v)

## From The Terminal

- gem install jekyll bundler

- bundle init

- gem "jekyll"
- gem install jekyll bundler
Create a new Gemfile to list your project’s dependencies:

bundle init
Edit the Gemfile in a text editor and add jekyll as a dependency:

gem "jekyll"
Run bundle to install jekyll for your project.

You can now prefix all jekyll commands listed in this tutorial with bundle exec to make sure you use the jekyll version defined in your Gemfile.

Create a sitePermalink
It’s time to create a site! Create a new directory for your site and name it whatever you want. Through the rest of this tutorial we’ll refer to this directory as root.

You can also initialize a Git repository here.

One of the great things about Jekyll is there’s no database. All content and site structure are files that a Git repository can version. Using a repository is optional but is recommended. You can learn more about using Git by reading the Git Handbook.

Let’s add your first file. Create index.html in root with the following content:

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Home</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>

BuildPermalink
Since Jekyll is a static site generator, it has to build the site before we can view it. Run either of the following commands to build your site:

jekyll build - Builds the site and outputs a static site to a directory called _site.
jekyll serve - Does jekyll build and runs it on a local web server at http://localhost:4000, rebuilding the site any time you make a change.


When you’re developing a site, use jekyll serve. To force the browser to refresh with every change, use jekyll serve --livereload. If there’s a conflict or you’d like Jekyll to serve your development site at a different URL, use the --host and --port arguments, as described in the serve command options.

The version of the site that jekyll serve builds in _site is not suited for deployment. Links and asset URLs in sites created with jekyll serve will use https://localhost:4000 or the value set with command-line configuration, instead of the values set in your site’s configuration file. To learn about how to build your site when it’s ready for deployment, read the Deployment section of this tutorial.

Run jekyll serve and go to http://localhost:4000 in your browser. You should see “Hello World!”.

At this point, you might be thinking, “So what?”. The only thing that happened was that Jekyll copied an HTML file from one place to another.

Patience, young grasshopper, there’s still much to learn!

Next. you’ll learn about Liquid and templating.

Step by Step Tutorial
2. Liquid
Liquid is where Jekyll starts to get more interesting. It is a templating language which has three main components:

objects
tags
filters
ObjectsPermalink
Objects tell Liquid to output predefined variables as content on a page. Use double curly braces for objects: {{ and }}.

For example, {{ page.title }} displays the page.title variable.

TagsPermalink
Tags define the logic and control flow for templates. Use curly braces and percent signs for tags: {% and %}.

For example:

{% if page.show_sidebar %}
  <div class="sidebar">
    sidebar content
  </div>
{% endif %}
This displays the sidebar if the value of the show_sidebar page variable is true.

Learn more about the tags available in Jekyll here.

FiltersPermalink
Filters change the output of a Liquid object. They are used within an output and are separated by a |.

For example:

{{ "hi" | capitalize }}
This displays Hi instead of hi.

Learn more about the filters available.

Use LiquidPermalink
Now, use Liquid to make your Hello World! text from Setup lowercase:

...
<h1>{{ "Hello World!" | downcase }}</h1>
...
To make Jekyll process your changes, add front matter to the top of the page:

---
# front matter tells Jekyll to process Liquid
---
Your HTML document should look like this:

---
---

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Home</title>
  </head>
  <body>
    <h1>{{ "Hello World!" | downcase }}</h1>
  </body>
</html>
When you reload your browser, you should see hello world!.

Much of Jekyll’s power comes from combining Liquid with other features. Add frontmatter to pages to make Jekyll process the Liquid on those pages.

Next, you’ll learn more about frontmatter.



- In the upper-right corner of any page, use the  drop-down menu, and select New repository.
- Enter username.github.io as the repository name. Replace username with your GitHub username. For example, if your username is octocat, the repository name should be octocat.github.io.
- Under your repository name, click  Settings.

- In the left sidebar, click Pages.
Click Choose a theme.
- The Theme Chooser will open. Browse the available themes, then click Select theme to select a theme. It's easy to change your theme later, so if you're not sure, just choose one for now.
- After you select a theme, your repository's README.md file will open in the file editor. The README.md file is where you will write the content for your site. You can edit the file or keep the default content for now.
- When you are done editing the file, click Commit changes.
- Visit username.github.io to view your new website. Note: It can take up to 20 minutes for changes to your site to publish after you push the changes to GitHub.


By default, the title of your site is username.github.io. You can change the title by editing the _config.yml file in your repository. You can also add a description for your site.

Click the Code tab of your repository.

In the file list, click _config.yml to open the file.

Click  to edit the file.

The _config.yml file already contains a line that specifies the theme for your site. Add a new line with title: followed by the title you want. Add a new line with description: followed by the description you want. For example:

theme: jekyll-theme-minimal
title: Octocat's homepage
description: Bookmark this to keep an eye on my project updates!
When you are done editing the file, click Commit changes.


## Ruby 101 

Jekyll is written in Ruby. If you’re new to Ruby, this page helps you learn some of the terminology.

GemsPermalink
Gems are code you can include in Ruby projects. Gems package specific functionality. You can share gems across multiple projects or with other people. Gems can perform actions like:

Converting a Ruby object to JSON
Pagination
Interacting with APIs such as GitHub
Jekyll is a gem. Many Jekyll plugins are also gems, including jekyll-feed, jekyll-seo-tag and jekyll-archives.

GemfilePermalink
A Gemfile is a list of gems used by your site. Every Jekyll site has a Gemfile in the main folder.

For a simple Jekyll site it might look something like this:

source "https://rubygems.org"

gem "jekyll"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
end
BundlerPermalink
Bundler is a gem that installs all gems in your Gemfile.

While you don’t have to use Gemfile and bundler, it is highly recommended as it ensures you’re running the same version of Jekyll and its plugins across different environments.

Install Bundler using gem install bundler. You only need to install it once, not every time you create a new Jekyll project.

To install gems in your Gemfile using Bundler, run the following in the directory that has the Gemfile:

bundle install
bundle exec jekyll serve
To bypass Bundler if you aren’t using a Gemfile, run jekyll serve.

See Using Jekyll with Bundler for more information about Bundler in Jekyll and for instructions to get up and running quickly.


