<template>
    <Counter />
    <Vbind />
    <Eventhandle />
</template>

<script>
import Counter from "./Counter"
import Vbind from "./Vbind"
import Eventhandle from "./Eventhandle"

export default {
    name: 'App',
    components: {
        Counter,
        Vbind,
        Eventhandle,
    },
    created() {        // use created keyword, NOT A METHOD to perform function immediately
        console.log("created function")
    }
}
</script>
