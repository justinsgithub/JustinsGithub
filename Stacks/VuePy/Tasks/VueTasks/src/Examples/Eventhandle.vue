<template>
    <div id="event-handling">
        <p>{{message}}</p>
        <button v-on:click="reverseMessage">
            Reverse Message
        </button>
    </div>
</template>

<script>
export default{
    name: "Eventhandle",
    data(){
        return {
            message: "This is a message returned by data()"
        }
    },
    methods: {
        reverseMessage() {
            this.message = this.message.split('').reverse().join('')
        }
    },
}
</script>
