   Link: preload
   Link: preload
   Link: preload
   Link: preload
   Link: preload
   Link: preload
   Tutorials References Exercises Videos NEW Menu
   Log in
   Paid Courses Website NEW
   HTML CSS JAVASCRIPT SQL PYTHON PHP BOOTSTRAP HOW TO W3.CSS JAVA JQUERY C++ C# R React Kotlin   
   ×

Tutorials

  HTML and CSS

    Learn HTML Learn CSS Learn RWD Learn Bootstrap Learn W3.CSS Learn Colors Learn Icons Learn Graphics Learn SVG Learn Canvas Learn How To Learn
   Sass

  Data Analytics

   Learn AI Learn Machine Learning Learn Data Science Learn NumPy Learn Pandas Learn SciPy Learn Matplotlib Learn Statistics Learn Excel

  XML Tutorials

   Learn XML Learn XML AJAX Learn XML DOM Learn XML DTD Learn XML Schema Learn XSLT Learn XPath Learn XQuery

  JavaScript

   Learn JavaScript Learn jQuery Learn React Learn AngularJS Learn JSON Learn AJAX Learn AppML Learn W3.JS

  Programming

   Learn Python Learn Java Learn C++ Learn C# Learn R Learn Kotlin Learn Go

  Server Side

   Learn SQL Learn MySQL Learn PHP Learn ASP Learn Node.js Learn Raspberry Pi Learn Git

  Web Building

     Create a Website NEW Web Templates Web Statistics Web Certificates Web Development Code Editor Test Your Typing Speed Play a Code Game Cyber
   Security Accessibility

  Data Analytics

     Learn AI Learn Machine Learning Learn Data Science Learn NumPy Learn Pandas Learn SciPy Learn Matplotlib Learn Statistics Learn Excel Learn
   Google Sheets

  XML Tutorials

   Learn XML Learn XML AJAX Learn XML DOM Learn XML DTD Learn XML Schema Learn XSLT Learn XPath Learn XQuery
   ×

References

  HTML

      HTML Tag Reference HTML Browser Support HTML Event Reference HTML Color Reference HTML Attribute Reference HTML Canvas Reference HTML SVG
   Reference Google Maps Reference

  CSS

      CSS Reference CSS Browser Support CSS Selector Reference Bootstrap 3 Reference Bootstrap 4 Reference W3.CSS Reference Icon Reference Sass
   Reference

  JavaScript

   JavaScript Reference HTML DOM Reference jQuery Reference AngularJS Reference AppML Reference W3.JS Reference

  Programming

   Python Reference Java Reference

  Server Side

   SQL Reference MySQL Reference PHP Reference ASP Reference

  XML

   XML DOM Reference XML Http Reference XSLT Reference XML Schema Reference

  Character Sets

   HTML Character Sets HTML ASCII HTML ANSI HTML Windows-1252 HTML ISO-8859-1 HTML Symbols HTML UTF-8
   ×

Exercises and Quizzes

  Exercises

   HTML Exercises CSS Exercises JavaScript Exercises SQL Exercises MySQL Exercises PHP Exercises Python Exercises NumPy Exercises Pandas Exercises
       SciPy Exercises jQuery Exercises Java Exercises C++ Exercises C# Exercises R Exercises Kotlin Exercises Go Exercises Bootstrap Exercises
   Bootstrap 4 Exercises Bootstrap 5 Exercises Git Exercises

  Quizzes

   HTML Quiz CSS Quiz JavaScript Quiz SQL Quiz MySQL Quiz PHP Quiz Python Quiz NumPy Quiz Pandas Quiz SciPy Quiz jQuery Quiz Java Quiz C++ Quiz C#
   Quiz R Quiz XML Quiz Cyber Security Quiz Bootstrap Quiz Bootstrap 4 Quiz Bootstrap 5 Quiz Accessibility Quiz

  Courses

    HTML Course CSS Course JavaScript Course Front End Course SQL Course PHP Course Python Course NumPy Course Pandas Course Data Analytics Course
   jQuery Course Java Course C++ Course C# Course R Course XML Course Cyber Security Course Accessibility Course

  Certificates

    HTML Certificate CSS Certificate JavaScript Certificate Front End Certificate SQL Certificate PHP Certificate Python Certificate Data Science
        Certificate Bootstrap 3 Certificate Bootstrap 4 Certificate jQuery Certificate Java Certificate C++ Certificate React Certificate XML
   Certificate
                                                                          ×
   Tutorials

   References

   Exercises

                                                           Paid Courses Spaces Videos Shop

Node.js Tutorial

   Node.js HOME Node.js Intro Node.js Get Started Node.js Modules Node.js HTTP Module Node.js File System Node.js URL Module Node.js NPM Node.js
   Events Node.js Upload Files Node.js Email

Node.js MySQL

   MySQL Get Started MySQL Create Database MySQL Create Table MySQL Insert Into MySQL Select From MySQL Where MySQL Order By MySQL Delete MySQL
   Drop Table MySQL Update MySQL Limit MySQL Join

Node.js MongoDB

   MongoDB Get Started MongoDB Create Database MongoDB Create Collection MongoDB Insert MongoDB Find MongoDB Query MongoDB Sort MongoDB Delete
   MongoDB Drop Collection MongoDB Update MongoDB Limit MongoDB Join

Raspberry Pi

   RasPi Get Started RasPi GPIO Introduction RasPi Blinking LED RasPi LED & Pushbutton RasPi Flowing LEDs RasPi WebSocket RasPi RGB LED WebSocket
   RasPi Components

Node.js Reference

   Built-in Modules

                                                                Node.js MongoDB Update

   ❮ Previous Next ❯

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Update Document

   You can update a record, or document as it is called in MongoDB, by using the updateOne() method.

   The first parameter of the updateOne() method is a query object defining which document to update.

   Note: If the query finds more than one record, only the first occurrence is updated.

   The second parameter is an object defining the new values of the document.

  Example

   Update the document with the address "Valley 345" to name="Mickey" and address="Canyon 123":

   var MongoClient = require('mongodb').MongoClient;
   var url = "mongodb://127.0.0.1:27017/";

   MongoClient.connect(url, function(err, db) {
     if (err) throw err;
     var dbo = db.db("mydb");
     var myquery = { address: "Valley 345" };
     var newvalues = { $set: {name: "Mickey", address: "Canyon 123" } };
     dbo.collection("customers").updateOne(myquery, newvalues, function(err, res) {
       if (err) throw err;
       console.log("1 document updated");
       db.close();
     });
   });
   Run example »

   Save the code above in a file called "demo_update_one.js" and run the file:

   Run "demo_update_one.js"

   C:\Users\Your Name>node demo_update_one.js

   Which will give you this result:

   1 document updated

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Update Only Specific Fields

   When using the $set operator, only the specified fields are updated:

  Example

   Update the address from "Valley 345" to "Canyon 123":

   ...
     var myquery = { address: "Valley 345" };
     var newvalues = { $set: { address: "Canyon 123" } };
     dbo.collection("customers").updateOne(myquery, newvalues, function(err, res) {
   ...
   Run example »

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

Update Many Documents

   To update all documents that meets the criteria of the query, use the updateMany() method.

  Example

   Update all documents where the name starts with the letter "S":

   var MongoClient = require('mongodb').MongoClient;
   var url = "mongodb://127.0.0.1:27017/";

   MongoClient.connect(url, function(err, db) {
     if (err) throw err;
     var dbo = db.db("mydb");
     var myquery = { address: /^S/ };
     var newvalues = {$set: {name: "Minnie"} };
     dbo.collection("customers").updateMany(myquery, newvalues, function(err, res) {
       if (err) throw err;
       console.log(res.result.nModified + " document(s) updated");
       db.close();
     });
   });
   Run example »

   Save the code above in a file called "demo_update_many.js" and run the file:

   Run "demo_update_many.js"

   C:\Users\Your Name>node demo_update_many.js

   Which will give you this result:

   2 document(s) updated

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

The Result Object

   The updateOne() and the updateMany() methods return an object which contains information about how the execution affected the database.

   Most of the information is not important to understand, but one object inside the object is called "result" which tells us if the execution went
   OK, and how many documents were affected.

   The result object looks like this:

   { n: 1, nModified: 2, ok: 1 }

   You can use this object to return the number of updated documents:

  Example

   Return the number of updated documents:

   console.log(res.result.nModified);

   Which will produce this result:

   2

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

   ❮ Previous Next ❯
                                                                         NEW

                                                                   We just launched
                                                                   W3Schools videos

                                                                  [IMG] Explore now

                                                                     COLOR PICKER

                                                                     colorpicker

                                                                       LIKE US

                                                                    Get certified
                                                                    by completing
                                                                   a course today!

                                                           w3schools  CERTIFIED   .   2021
                                                                     Get started

                                                                      CODE GAME

                                                                 Code Game Play Game

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

                                                                     Report Error
                                                                        Forum
                                                                        About
                                                                         Shop

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

   ×

Report Error

   If you want to report an error, or if you want to make a suggestion, do not hesitate to send us an e-mail:

   help@w3schools.com

   ×

Thank You For Helping Us!

   Your message has been sent to W3Schools.

                                                                    Top Tutorials

                                                                    HTML Tutorial
                                                                     CSS Tutorial
                                                                 JavaScript Tutorial
                                                                   How To Tutorial
                                                                     SQL Tutorial
                                                                   Python Tutorial
                                                                   W3.CSS Tutorial
                                                                  Bootstrap Tutorial
                                                                     PHP Tutorial
                                                                    Java Tutorial
                                                                     C++ Tutorial
                                                                   jQuery Tutorial

                                                                    Top References

                                                                    HTML Reference
                                                                    CSS Reference
                                                                 JavaScript Reference
                                                                    SQL Reference
                                                                   Python Reference
                                                                   W3.CSS Reference
                                                                 Bootstrap Reference
                                                                    PHP Reference
                                                                     HTML Colors
                                                                    Java Reference
                                                                  Angular Reference
                                                                   jQuery Reference

                                                                     Top Examples

                                                                    HTML Examples
                                                                     CSS Examples
                                                                 JavaScript Examples
                                                                   How To Examples
                                                                     SQL Examples
                                                                   Python Examples
                                                                   W3.CSS Examples
                                                                  Bootstrap Examples
                                                                     PHP Examples
                                                                    Java Examples
                                                                     XML Examples
                                                                   jQuery Examples

                                                                     Web Courses

                                                                     HTML Course
                                                                      CSS Course
                                                                  JavaScript Course
                                                                   Front End Course
                                                                      SQL Course
                                                                    Python Course
                                                                      PHP Course
                                                                    jQuery Course
                                                                     Java Course
                                                                      C++ Course
                                                                      C# Course
                                                                      XML Course
                                                                   Get Certified »

   ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

      W3Schools is optimized for learning and training. Examples might be simplified to improve reading and learning. Tutorials, references, and
     examples are constantly reviewed to avoid errors, but we cannot warrant full correctness of all content. While using W3Schools, you agree to
                                         have read and accepted our terms of use, cookie and privacy policy.

                                              Copyright 1999-2021 by Refsnes Data. All Rights Reserved.
                                                           W3Schools is Powered by W3.CSS.

References

   Visible links
   . https://www.w3schools.com/lib/fonts/fontawesome.woff2?14663396
   . https://www.w3schools.com/lib/fonts/source-code-pro-v14-latin-regular.woff2
   . https://www.w3schools.com/lib/fonts/roboto-mono-v13-latin-500.woff2
   . https://www.w3schools.com/lib/fonts/source-sans-pro-v14-latin-700.woff2
   . https://www.w3schools.com/lib/fonts/source-sans-pro-v14-latin-600.woff2
   . https://www.w3schools.com/lib/fonts/freckle-face-v9-latin-regular.woff2
   . Tutorials
	javascript:void(0)
   . Video Tutorials
	https://www.w3schools.com/videos/index.php
   . Menu
	javascript:void(0)
   . https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com
   . Courses
	https://courses.w3schools.com/
   . Get Your Own Website With W3shools Spaces
	https://www.w3schools.com/spaces
   . HTML Tutorial
	https://www.w3schools.com/html/default.asp
   . CSS Tutorial
	https://www.w3schools.com/css/default.asp
   . JavaScript Tutorial
	https://www.w3schools.com/js/default.asp
   . SQL Tutorial
	https://www.w3schools.com/sql/default.asp
   . Python Tutorial
	https://www.w3schools.com/python/default.asp
   . PHP Tutorial
	https://www.w3schools.com/php/default.asp
   . Bootstrap Tutorial
	https://www.w3schools.com/bootstrap/bootstrap_ver.asp
   . How To
	https://www.w3schools.com/howto/default.asp
   . W3.CSS Tutorial
	https://www.w3schools.com/w3css/default.asp
   . Java Tutorial
	https://www.w3schools.com/java/default.asp
   . jQuery Tutorial
	https://www.w3schools.com/jquery/default.asp
   . C++ Tutorial
	https://www.w3schools.com/cpp/default.asp
   . C# Tutorial
	https://www.w3schools.com/cs/index.php
   . R Tutorial
	https://www.w3schools.com/r/default.asp
   . React Tutorial
	https://www.w3schools.com/react/default.asp
   . Kotlin Tutorial
	https://www.w3schools.com/kotlin/index.php
   . Search W3Schools
	javascript:void(0);
   . Translate W3Schools
	javascript:void(0);
   . Toggle Dark Code
	javascript:void(0);
   . https://www.w3schools.com/html/default.asp
   . https://www.w3schools.com/css/default.asp
   . Responsive Web Design
	https://www.w3schools.com/css/css_rwd_intro.asp
   . https://www.w3schools.com/bootstrap/bootstrap_ver.asp
   . https://www.w3schools.com/w3css/default.asp
   . https://www.w3schools.com/colors/default.asp
   . https://www.w3schools.com/icons/default.asp
   . https://www.w3schools.com/graphics/default.asp
   . https://www.w3schools.com/graphics/svg_intro.asp
   . https://www.w3schools.com/graphics/canvas_intro.asp
   . https://www.w3schools.com/howto/default.asp
   . https://www.w3schools.com/sass/default.php
   . https://www.w3schools.com/ai/default.asp
   . https://www.w3schools.com/python/python_ml_getting_started.asp
   . https://www.w3schools.com/datascience/default.asp
   . https://www.w3schools.com/python/numpy/default.asp
   . https://www.w3schools.com/python/pandas/default.asp
   . https://www.w3schools.com/python/scipy/index.php
   . https://www.w3schools.com/python/matplotlib_intro.asp
   . https://www.w3schools.com/statistics/index.php
   . https://www.w3schools.com/excel/index.php
   . https://www.w3schools.com/xml/default.asp
   . https://www.w3schools.com/xml/ajax_intro.asp
   . https://www.w3schools.com/xml/dom_intro.asp
   . https://www.w3schools.com/xml/xml_dtd_intro.asp
   . https://www.w3schools.com/xml/schema_intro.asp
   . https://www.w3schools.com/xml/xsl_intro.asp
   . https://www.w3schools.com/xml/xpath_intro.asp
   . https://www.w3schools.com/xml/xquery_intro.asp
   . https://www.w3schools.com/js/default.asp
   . https://www.w3schools.com/jquery/default.asp
   . https://www.w3schools.com/react/default.asp
   . https://www.w3schools.com/angular/default.asp
   . https://www.w3schools.com/js/js_json_intro.asp
   . https://www.w3schools.com/js/js_ajax_intro.asp
   . https://www.w3schools.com/appml/default.asp
   . https://www.w3schools.com/w3js/default.asp
   . https://www.w3schools.com/python/default.asp
   . https://www.w3schools.com/java/default.asp
   . https://www.w3schools.com/cpp/default.asp
   . https://www.w3schools.com/cs/index.php
   . https://www.w3schools.com/r/default.asp
   . https://www.w3schools.com/kotlin/index.php
   . https://www.w3schools.com/go/index.php
   . https://www.w3schools.com/sql/default.asp
   . https://www.w3schools.com/mysql/default.asp
   . https://www.w3schools.com/php/default.asp
   . https://www.w3schools.com/asp/default.asp
   . https://www.w3schools.com/nodejs/default.asp
   . https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp
   . https://www.w3schools.com/git/default.asp
   . Get Your Own Website With W3shools Spaces
	https://www.w3schools.com/spaces
   . https://www.w3schools.com/w3css/w3css_templates.asp
   . https://www.w3schools.com/browsers/default.asp
   . https://www.w3schools.com/cert/default.asp
   . https://www.w3schools.com/whatis/default.asp
   . https://www.w3schools.com/tryit/default.asp
   . https://www.w3schools.com/typingspeed/default.asp
   . https://www.w3schools.com/codegame/index.html
   . https://www.w3schools.com/cybersecurity/index.php
   . https://www.w3schools.com/accessibility/index.php
   . https://www.w3schools.com/ai/default.asp
   . https://www.w3schools.com/python/python_ml_getting_started.asp
   . https://www.w3schools.com/datascience/default.asp
   . https://www.w3schools.com/python/numpy/default.asp
   . https://www.w3schools.com/python/pandas/default.asp
   . https://www.w3schools.com/python/scipy/index.php
   . https://www.w3schools.com/python/matplotlib_intro.asp
   . https://www.w3schools.com/statistics/index.php
   . https://www.w3schools.com/excel/index.php
   . https://www.w3schools.com/googlesheets/index.php
   . https://www.w3schools.com/xml/default.asp
   . https://www.w3schools.com/xml/ajax_intro.asp
   . https://www.w3schools.com/xml/dom_intro.asp
   . https://www.w3schools.com/xml/xml_dtd_intro.asp
   . https://www.w3schools.com/xml/schema_intro.asp
   . https://www.w3schools.com/xml/xsl_intro.asp
   . https://www.w3schools.com/xml/xpath_intro.asp
   . https://www.w3schools.com/xml/xquery_intro.asp
   . https://www.w3schools.com/tags/default.asp
   . https://www.w3schools.com/tags/ref_html_browsersupport.asp
   . https://www.w3schools.com/tags/ref_eventattributes.asp
   . https://www.w3schools.com/colors/default.asp
   . https://www.w3schools.com/tags/ref_attributes.asp
   . https://www.w3schools.com/tags/ref_canvas.asp
   . https://www.w3schools.com/graphics/svg_reference.asp
   . https://www.w3schools.com/graphics/google_maps_reference.asp
   . https://www.w3schools.com/cssref/default.asp
   . https://www.w3schools.com/cssref/css3_browsersupport.asp
   . https://www.w3schools.com/cssref/css_selectors.asp
   . https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp
   . https://www.w3schools.com/bootstrap4/bootstrap_ref_all_classes.asp
   . https://www.w3schools.com/w3css/w3css_references.asp
   . https://www.w3schools.com/icons/icons_reference.asp
   . https://www.w3schools.com/sass/sass_functions_string.php
   . https://www.w3schools.com/jsref/default.asp
   . https://www.w3schools.com/jsref/default.asp
   . https://www.w3schools.com/jquery/jquery_ref_overview.asp
   . https://www.w3schools.com/angular/angular_ref_directives.asp
   . https://www.w3schools.com/appml/appml_reference.asp
   . https://www.w3schools.com/w3js/w3js_references.asp
   . https://www.w3schools.com/python/python_reference.asp
   . https://www.w3schools.com/java/java_ref_keywords.asp
   . https://www.w3schools.com/sql/sql_ref_keywords.asp
   . https://www.w3schools.com/mysql/mysql_ref_functions.asp
   . https://www.w3schools.com/php/php_ref_overview.asp
   . https://www.w3schools.com/asp/asp_ref_response.asp
   . https://www.w3schools.com/xml/dom_nodetype.asp
   . https://www.w3schools.com/xml/dom_http.asp
   . https://www.w3schools.com/xml/xsl_elementref.asp
   . https://www.w3schools.com/xml/schema_elements_ref.asp
   . https://www.w3schools.com/charsets/default.asp
   . https://www.w3schools.com/charsets/ref_html_ascii.asp
   . https://www.w3schools.com/charsets/ref_html_ansi.asp
   . https://www.w3schools.com/charsets/ref_html_ansi.asp
   . https://www.w3schools.com/charsets/ref_html_8859.asp
   . https://www.w3schools.com/charsets/ref_html_symbols.asp
   . https://www.w3schools.com/charsets/ref_html_utf8.asp
   . https://www.w3schools.com/exercises/index.php
   . https://www.w3schools.com/html/html_exercises.asp
   . https://www.w3schools.com/css/css_exercises.asp
   . https://www.w3schools.com/js/js_exercises.asp
   . https://www.w3schools.com/sql/sql_exercises.asp
   . https://www.w3schools.com/mysql/mysql_exercises.asp
   . https://www.w3schools.com/php/php_exercises.asp
   . https://www.w3schools.com/python/python_exercises.asp
   . https://www.w3schools.com/python/numpy/numpy_exercises.asp
   . https://www.w3schools.com/python/pandas/pandas_exercises.asp
   . https://www.w3schools.com/python/scipy/scipy_exercises.php
   . https://www.w3schools.com/jquery/jquery_exercises.asp
   . https://www.w3schools.com/java/java_exercises.asp
   . https://www.w3schools.com/cpp/cpp_exercises.asp
   . https://www.w3schools.com/cs/cs_exercises.asp
   . https://www.w3schools.com/r/r_exercises.asp
   . https://www.w3schools.com/kotlin/kotlin_exercises.php
   . https://www.w3schools.com/go/go_exercises.php
   . https://www.w3schools.com/bootstrap/bootstrap_exercises.asp
   . https://www.w3schools.com/bootstrap4/bootstrap_exercises.asp
   . https://www.w3schools.com/bootstrap5/bootstrap_exercises.php
   . https://www.w3schools.com/git/git_exercises.asp
   . https://www.w3schools.com/quiztest/default.asp
   . https://www.w3schools.com/html/html_quiz.asp
   . https://www.w3schools.com/css/css_quiz.asp
   . https://www.w3schools.com/js/js_quiz.asp
   . https://www.w3schools.com/sql/sql_quiz.asp
   . https://www.w3schools.com/mysql/mysql_quiz.asp
   . https://www.w3schools.com/php/php_quiz.asp
   . https://www.w3schools.com/python/python_quiz.asp
   . https://www.w3schools.com/python/numpy/numpy_quiz.asp
   . https://www.w3schools.com/python/pandas/pandas_quiz.asp
   . https://www.w3schools.com/python/scipy/scipy_quiz.php
   . https://www.w3schools.com/jquery/jquery_quiz.asp
   . https://www.w3schools.com/java/java_quiz.asp
   . https://www.w3schools.com/cpp/cpp_quiz.asp
   . https://www.w3schools.com/cs/cs_quiz.asp
   . https://www.w3schools.com/r/r_quiz.asp
   . https://www.w3schools.com/xml/xml_quiz.asp
   . https://www.w3schools.com/cybersecurity/cybersecurity_quiz.php
   . https://www.w3schools.com/bootstrap/bootstrap_quiz.asp
   . https://www.w3schools.com/bootstrap4/bootstrap_quiz.asp
   . https://www.w3schools.com/bootstrap5/bootstrap_quiz.php
   . https://www.w3schools.com/accessibility/accessibility_quiz.php
   . https://courses.w3schools.com/
   . https://courses.w3schools.com/courses/html
   . https://courses.w3schools.com/courses/css
   . https://courses.w3schools.com/courses/javascript
   . https://courses.w3schools.com/programs/front-end
   . https://courses.w3schools.com/courses/sql
   . https://courses.w3schools.com/courses/php
   . https://courses.w3schools.com/courses/python
   . https://courses.w3schools.com/courses/numpy-fundamentals
   . https://courses.w3schools.com/courses/pandas-fundamentals
   . https://courses.w3schools.com/programs/data-analytics
   . https://courses.w3schools.com/courses/jquery
   . https://courses.w3schools.com/courses/java
   . https://courses.w3schools.com/courses/cplusplus
   . https://courses.w3schools.com/courses/c-sharp
   . https://courses.w3schools.com/courses/r-fundamentals
   . https://courses.w3schools.com/courses/xml
   . https://courses.w3schools.com/courses/introduction-to-cyber-security
   . https://courses.w3schools.com/courses/accessibility-fundamentals
   . https://courses.w3schools.com/browse/certifications
   . https://courses.w3schools.com/browse/certifications/courses/html-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/css-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/javascript-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/front-end-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/sql-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/php-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/python-certificaftion-exam
   . https://courses.w3schools.com/browse/certifications/courses/data-science-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/bootstrap-3-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/bootstrap-4-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/jquery-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/java-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/c-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/react-certification-exam
   . https://courses.w3schools.com/browse/certifications/courses/xml-certification-exam
   . javascript:void(0)
   . javascript:void(0);
   . https://www.w3schools.com/cert/default.asp
   . Get Your Own Website With W3shools Spaces
	https://www.w3schools.com/spaces
   . Video Tutorials
	https://www.w3schools.com/videos/index.php
   . https://shop.w3schools.com/
   . https://www.w3schools.com/nodejs/default.asp
   . https://www.w3schools.com/nodejs/nodejs_intro.asp
   . https://www.w3schools.com/nodejs/nodejs_get_started.asp
   . https://www.w3schools.com/nodejs/nodejs_modules.asp
   . https://www.w3schools.com/nodejs/nodejs_http.asp
   . https://www.w3schools.com/nodejs/nodejs_filesystem.asp
   . https://www.w3schools.com/nodejs/nodejs_url.asp
   . https://www.w3schools.com/nodejs/nodejs_npm.asp
   . https://www.w3schools.com/nodejs/nodejs_events.asp
   . https://www.w3schools.com/nodejs/nodejs_uploadfiles.asp
   . https://www.w3schools.com/nodejs/nodejs_email.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_create_db.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_create_table.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_insert.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_select.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_where.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_orderby.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_delete.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_drop_table.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_update.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_limit.asp
   . https://www.w3schools.com/nodejs/nodejs_mysql_join.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_create_db.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_createcollection.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_insert.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_find.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_query.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_sort.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_delete.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_drop.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_update.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_limit.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_join.asp
   . https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp
   . https://www.w3schools.com/nodejs/nodejs_raspberrypi_gpio_intro.asp
   . https://www.w3schools.com/nodejs/nodejs_raspberrypi_blinking_led.asp
   . https://www.w3schools.com/nodejs/nodejs_raspberrypi_led_pushbutton.asp
   . https://www.w3schools.com/nodejs/nodejs_raspberrypi_flowing_leds.asp
   . https://www.w3schools.com/nodejs/nodejs_raspberrypi_webserver_websocket.asp
   . https://www.w3schools.com/nodejs/nodejs_raspberrypi_rgb_led_websocket.asp
   . https://www.w3schools.com/nodejs/nodejs_raspberrypi_components.asp
   . https://www.w3schools.com/nodejs/ref_modules.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_drop.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_limit.asp
   . https://www.w3schools.com/nodejs/shownodejs_cmd.asp?filename=demo_update_one
   . https://www.w3schools.com/nodejs/shownodejs_cmd.asp?filename=demo_update_set
   . https://www.w3schools.com/nodejs/shownodejs_cmd.asp?filename=demo_update_many
   . https://www.w3schools.com/nodejs/nodejs_mongodb_drop.asp
   . https://www.w3schools.com/nodejs/nodejs_mongodb_limit.asp
   . https://www.w3schools.com/videos/index.php
   . https://www.w3schools.com/videos/index.php
   . https://www.w3schools.com/colors/colors_picker.asp
   . https://www.w3schools.com/colors/colors_picker.asp
   . https://courses.w3schools.com/
   . https://www.w3schools.com/codegame/index.html
   . https://www.w3schools.com/codegame/index.html
   . https://www.w3schools.com/codegame/index.html
   . javascript:void(0);
   . https://www.w3schools.com/forum/default.asp
   . https://www.w3schools.com/about/default.asp
   . https://shop.w3schools.com/
   . https://www.w3schools.com/html/default.asp
   . https://www.w3schools.com/css/default.asp
   . https://www.w3schools.com/js/default.asp
   . https://www.w3schools.com/howto/default.asp
   . https://www.w3schools.com/sql/default.asp
   . https://www.w3schools.com/python/default.asp
   . https://www.w3schools.com/w3css/default.asp
   . https://www.w3schools.com/bootstrap/bootstrap_ver.asp
   . https://www.w3schools.com/php/default.asp
   . https://www.w3schools.com/java/default.asp
   . https://www.w3schools.com/cpp/default.asp
   . https://www.w3schools.com/jquery/default.asp
   . https://www.w3schools.com/tags/default.asp
   . https://www.w3schools.com/cssref/default.asp
   . https://www.w3schools.com/jsref/default.asp
   . https://www.w3schools.com/sql/sql_ref_keywords.asp
   . https://www.w3schools.com/python/python_reference.asp
   . https://www.w3schools.com/w3css/w3css_references.asp
   . https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp
   . https://www.w3schools.com/php/php_ref_overview.asp
   . https://www.w3schools.com/colors/colors_names.asp
   . https://www.w3schools.com/java/java_ref_keywords.asp
   . https://www.w3schools.com/angular/angular_ref_directives.asp
   . https://www.w3schools.com/jquery/jquery_ref_overview.asp
   . https://www.w3schools.com/html/html_examples.asp
   . https://www.w3schools.com/css/css_examples.asp
   . https://www.w3schools.com/js/js_examples.asp
   . https://www.w3schools.com/howto/default.asp
   . https://www.w3schools.com/sql/sql_examples.asp
   . https://www.w3schools.com/python/python_examples.asp
   . https://www.w3schools.com/w3css/w3css_examples.asp
   . https://www.w3schools.com/bootstrap/bootstrap_examples.asp
   . https://www.w3schools.com/php/php_examples.asp
   . https://www.w3schools.com/java/java_examples.asp
   . https://www.w3schools.com/xml/xml_examples.asp
   . https://www.w3schools.com/jquery/jquery_examples.asp
   . https://courses.w3schools.com/courses/html
   . https://courses.w3schools.com/courses/css
   . https://courses.w3schools.com/courses/javascript
   . https://courses.w3schools.com/programs/front-end
   . https://courses.w3schools.com/courses/sql
   . https://courses.w3schools.com/courses/python
   . https://courses.w3schools.com/courses/php
   . https://courses.w3schools.com/courses/jquery
   . https://courses.w3schools.com/courses/java
   . https://courses.w3schools.com/courses/cplusplus
   . https://courses.w3schools.com/courses/c-sharp
   . https://courses.w3schools.com/courses/xml
   . https://courses.w3schools.com/
   . https://www.w3schools.com/about/about_copyright.asp
   . https://www.w3schools.com/about/about_privacy.asp
   . https://www.w3schools.com/about/about_copyright.asp
   . https://www.w3schools.com/w3css/default.asp
