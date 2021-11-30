<template>
<div id="bind-attribute">
    <span v-bind:title="message">
        Hover the mouse to see v-binded title 
    </span>
</div>
</template>

<script>
export default {
    name: "Vbind",
    data(){
        return {
            message: "This page was loaded in " + new Date().toLocaleString()
        }
    }
}
</script>
