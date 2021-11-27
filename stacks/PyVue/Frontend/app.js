/*
const app = Vue.createApp({
    template: "<h1>Hello World</h1>"
})
const app = Vue.createApp({
    template: "<h1>Hello {{myObject}}</h1>",
    data(){
        return {
            myObject: "World",
        }
    }
})
*/

const app = Vue.createApp({
    data(){
        return {
            firstName: "John",
            lastName: "Doe",
            email: "john@example.com",
            gender: "male",
            picture: "https://randomuser.me/api/portraits/men/10.jpg",
            userRequests: '',

            firstName2: "Jane",
            lastName2: "Doe",
            email2: "jane@example.com",
            gender2: "female",
            picture2: "https://randomuser.me/api/portraits/women/8.jpg",
        }
    },
    methods: {
        async getUser(){
            const response = await fetch('http://127.0.0.1:3000/randomuser')
            const {results} = await response.json()
            const response2 = await fetch('http://127.0.0.1:3000/randomusernum')
            const results2 = await response2.json()
            console.log(results2)

            this.firstName = results[0].name.first
            this.lastName = results[0].name.last
            this.email = results[0].email
            this.gender = results[0].gender
            this.picture = results[0].picture.large
            this.userRequests = results2.numOfRequests
        }
    }
})
app.mount("#app")
