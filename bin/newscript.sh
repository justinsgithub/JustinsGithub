#!/bin/bash

echo 'enter new script name > '

read scriptName

touch /bin/$scriptName

chmod +x /bin/$scriptName

echo '#!/bin/bash' > /bin/$scriptName

vim /bin/$scriptName
