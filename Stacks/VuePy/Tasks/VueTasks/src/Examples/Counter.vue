<template>

<div id="counter">
  this is a counter using return value from data function: {{ counter }}
</div>
</template>

<script>
export default {
  name: "Counter",
  data(){
    return {
      counter: 5
    }
  },
  mounted(){
    setInterval(() => {
      this.counter++
    }, 1000)
  }
}
</script>
