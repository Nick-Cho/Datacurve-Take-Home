## Build and Run Steps
### Frontend
``` npm i ``` - to install dependencies for application
``` npm run dev ``` - to run the Frontend application

### Backend
``` pip install requirements.txt``` - to install dependencies necessary for backend server
``` fastapi dev src/main.py ``` - runs the backend server
Fill in the details in the ```database.py``` file to match your SQL database.
Run the script in the ```create_db.py``` to initalize the database

## Approach
<img width="1066" alt="image" src="https://github.com/Nick-Cho/Datacurve-Take-Home/assets/65980644/ac3a5ac6-8d54-4f46-8da9-efbb67f118d3">

### Security Measures
Instead of running code in a sandbox environment like most online code ide's I chose to use **docker containers** instead due to their ease of managing the packages (pandas and scipy) that 
were required for the assignment along with the lightweight and easy setup of docker. This allowed me to run my code in an isolated environment that wouldn't harm the execution of my server directly.
Some additional concerns:
1. **Infinite Loop** - Would stall the server and make it unable to service other requests. Accounted for this by adding a **timeout** on the code execution in the Docker container.
2. **File System Access** - Would allow user to change potentially important server files. Accounted for this by executing code with non-root user in the Docker container.
3. **Privellege Escalation** - Would also allow user to read/write to private files. Accounted for this by explicitly giving read permissions to only the file holding the user code to execute.
4. **Network Access** - Would allow user to make requests on behalf of the server. Disabled network access in the container.

### Database Design
<img width="812" alt="image" src="https://github.com/Nick-Cho/Datacurve-Take-Home/assets/65980644/a87c14c3-193f-4a89-8174-3b53dbe5e102">

