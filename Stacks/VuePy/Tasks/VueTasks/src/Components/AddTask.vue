<template>
  <form @submit="onSubmit" class="add-form">

    <div class="form-control">
      <label>Task</label>
      <input type="text" v-model="text" name="text" placeholder="Add Task" />
    </div>

    <div class="form-control">
      <label>Day & Time</label>
      <input type="text" v-model="day" name="day" placeholder="Add Day & Time" />
    </div>

    <div class="form-control form-control-check">
      <label>Set Reminder</label>
      <input type="checkbox" v-model="reminder" name="reminder" />
    </div>

    <input type="submit" value="Save Task" class="btn btn-block" />

  </form>
</template>

<script>
export default {
    name: "AddTask",
    data(){
        return {
            text: "",
            day: "",
            reminder: false
        }
    },

    methods: {        // @onSubmit = IMPORTANT onSubmit NOT onSubmit()
        onSubmit(e) {
            e.preventDefault() // prevent the form from performing the default submit event when button is clicked
            if(!this.text){  // if no text in v-model binding, prompt user, end function
                alert("No task to add")
                return
            }
            if(!this.day){ // if no date is added comfirm with user, continue function
                confirm("No date is going to be added")
            }
            const newTask = { // create newTask object from v-binded form inputs
                //id: Math.floor(Math.random() * 1000000),
                text: this.text,
                day: this.day,
                reminder: this.reminder
            }
            // emit 'add-task function to App.vue and pass that function the newTask'
            this.$emit('add-task', newTask)
            // console.log(newTask) // test
            // reset all form inputs so it's reset for a new task
            this.text = ""
            this.day = ""
            this.reminder = false
        }
    }
}
</script>

<style scoped>
.btn-block{
    display: block;
    width: 100%;
}
.add-form {
  margin-bottom: 40px;
}
.form-control {
  margin: 20px 0;
}
.form-control label {
  display: block;
}
.form-control input {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}
.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.form-control-check label {
  flex: 1;
}
.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>
