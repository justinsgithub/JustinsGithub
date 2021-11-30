    <div class="container">
        <Header
                :showAddTask="showAddTask"
                title="Task Tracker"
                @toggle-add-task="toggleAddTask"
        />
        <div v-show="showAddTask">
            <AddTask @add-task="addTask"/>
        </div>

        <Tasks
                :tasks="tasks"
                @toggle-reminder="toggleReminder"
                @delete-task="deleteTask"
        />
    </div>
</template>

<script>

// import components being used in this component

import Header from './components/Header'
import Tasks from './components/Tasks'
import AddTask from './components/AddTask'

// export this component as an  object with all the information needed for our component
export default {
    name: 'App',

// IMPORTANT, register the above imported components in our exported object
    components: {
        Header,
        Tasks,
        AddTask,
    },
    data() {
        return {
            tasks: [],
            showAddTask: false,
        }
    },
    methods: {
        toggleAddTask() {
            console.log("toggleAddTask method")
            this.showAddTask = !this.showAddTask
        },
        async addTask(task) {
            console.log("addTask method")
            const head = { "Content-Type": "application/json"}
            const init =  { method: "POST", header:head }
            const response = await fetch("http://localhost:5000/tasks", {
                init,
                body:JSON.stringify(task),
            })
            const data = await response.json
            this.tasks = [...this.tasks, data]
        },
        async deleteTask(id) {
            console.log("deleteTask method")
            const init = {method:"DELETE"}
            if (confirm('Are you sure?')) {
                const response = await fetch(`http://localhost:5000/tasks/${id}`, init)
                response.status === 200
                    ? this.tasks = this.tasks.filter((task) => task.id !== id)
                    : alert("error, task not deleted")
            }
        },
        async toggleReminder(id) {
            console.log("toggleReminder method")
            const toggleThisTask = await this.fetchTask(id)
            const updateTask = {...toggleThisTask, reminder: !toggleThisTask.reminder}
            const head = {"Content-Type": "application/json"}
            const bod = JSON.stringify(updateTask)
            const init = {method:"PUT", headers: head, body:bod}
            const response = await fetch(`http://localhost:5000/tasks/${id}`, init)
            const data = await response.json()

            this.tasks = this.tasks.map(
                (task) => task.id === id ? {...task, reminder: data.reminder} : task
            )
        },
        async fetchTask(id) {
            console.log("fetchTask method")
            const response = await fetch(`http://localhost:5000/tasks/${id}`)
            const data = await response.json()
            console.log(data)
            return data
        },
        async fetchTasks() {
            console.log("fetchTasks method")
            const response = await fetch("http://localhost:5000/tasks")
            const data = await response.json()
            console.log(data)
            return data
        }
    },
    async created() {        // use created keyword, NOT A METHOD to perform function immediately
        console.log("created function")
        this.tasks = await this.fetchTasks()
    }
}
</script>

<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Poppins', sans-serif;
}

.container {
    max-width: 500px;
    margin: 30px auto;
    overflow: auto;
    min-height: 300px;
    border: 1px solid steelblue;
    padding: 30px;
    border-radius: 5px;
}


</style>
