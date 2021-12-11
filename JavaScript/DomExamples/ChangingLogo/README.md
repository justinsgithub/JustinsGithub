- HTML creates the skeleton of a webpage, but JavaScript introduces interactivity

- The `<script>` element has an opening and closing tag. You can embed JavaScript code inbetween the opening and closing `<script>` tags.

- You link to external JavaScript files with the src attribute in the opening `<script>` tag.

- By default, scripts are loaded and executed as soon as the HTML parser encounters them in the HTML file, the HTML parser waits to load the entire script before from proceeding to parse the rest of the page elements.

- The defer attribute ensures that the entire HTML file has been parsed before the script is executed.

- The async attribute will allow the HTML parser to continue parsing as the script is being downloaded, but will execute immediately after it has been downloaded.
