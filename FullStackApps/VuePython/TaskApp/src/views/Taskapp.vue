<template>
  <div class="container">
  <Header
      @toggle-add-task="toggleAddTask"
      title="Task Tracker"
      :showAddTask="showAddTask"
    />
  <AddTask v-show="showAddTask" @add-task="addTask" />
  <Tasks
    @toggle-reminder="toggleReminder"
    @delete-task="deleteTask"
    :tasks="tasks"
  />
  </div>
</template>

<script>
import Header from '@/components/Header'
import Tasks from '@/components/Tasks'
import AddTask from '@/components/AddTask'

export default {
  name: 'Taskapp',
  components: {
    Header,
    Tasks,
    AddTask
  },
  data () {
    return {
      tasks: [],
      showAddTask: false
    }
  },
  methods: {
    toggleAddTask () {
      this.showAddTask = !this.showAddTask
    },
    async addTask (task) {
      const res = await fetch('http://localhost:5000/tasks', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(task)
      })

      const data = await res.json()

      this.tasks = [...this.tasks, data]
    },
    async deleteTask (id) {
      if (confirm('Are you sure?')) {
        const res = await fetch(`http://localhost:5000/tasks/${id}`, {
          method: 'DELETE'
        })

        res.status === 200
          ? (this.tasks = this.tasks.filter((task) => task.id !== id))
          : alert('Error deleting task')
      }
    },
    async toggleReminder (id) {
      const taskToToggle = await this.fetchTask(id)
      const updTask = { ...taskToToggle, reminder: !taskToToggle.reminder }

      const res = await fetch(`http://localhost:5000/tasks/${id}`, {
        method: 'PUT',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(updTask)
      })

      const data = await res.json()

      this.tasks = this.tasks.map((task) =>
        task.id === id ? { ...task, reminder: data.reminder } : task
      )
    },
    async fetchTasks () {
      const res = await fetch('http://localhost:5000/tasks')

      return res.json()
    },
    async fetchTask (id) {
      const res = await fetch(`http://localhost:5000/tasks/${id}`)

      return res.json()
    }
  },
  async created () {
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
