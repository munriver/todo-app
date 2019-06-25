<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

    <p v-if="currentUser">
      Logged in as <b>{{ currentUser }}</b>.
      <a href="#" @click="logout">Logout</a>
    </p>
    <p v-else>
      <label>Login: </label>
      <input type="text" placeholder="username" v-model="uname">
      <input type="password" placeholder="password" v-model="passwd">
      <button @click="login">></button>
      <br>
    </p>

    <br>
    <h2>Tasks</h2>
    <ul>
      <li v-for="task in taskList"
          v-bind:class="{ completed: task.complete_status,
                          editing: task.id == taskEditState }"
          v-bind:key="task.id">
        <div class="tview">
          <input v-model="task.complete_status" type="checkbox"
               @click="markCompleted(task)">
            <label>{{ task.title }}</label>
          <button class="deletebtn" @click="deleteTask(task.id)">x</button>
          <button class="editbtn" @click="editTask(task)">e</button>
        </div>
        <input class="edit" type="text" v-model="task.title"
               @keyup.enter="doneEditTask(task)"
               @keyup.esc="cancelEditTask">
        <input class="edit" type="checkbox" v-model="task.private"
               @click="doneEditTask(task)" name="pvt">
        <label class="edit" for="pvt">private</label>
      </li>
    </ul>

    <p>
      <input class="addtask" placeholder="Add new todo" v-model="newTask"
             @keyup.enter="addTask">
      <button class="addtaskbtn" @click="addTask">+</button>
    </p>
  </div>
</template>

<script>
import axios from 'axios'
const apiUrl = 'http://localhost:8000'
export default {
  name: 'Home',
  data () {
    return {
      msg: 'TODO App',
      taskList: [],
      errors: [],
      taskEditState: null,
      newTask: '',

      uname: '',
      passwd: '',
      csrfToken: '',
      currentUser: ''
    }
  },
  methods: {
    getFromBackend () {
      const path = `${apiUrl}/todolist/`
      this.getCurrentUser()
      axios({
        method: 'get',
        url: path,
        withCredentials: true
      })
        .then(response => {
          this.taskList = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    markCompleted (task) {
      const path = `${apiUrl}/todolist/${task.id}/`
      task.complete_status = !task.complete_status
      axios.put(path, task, {
        withCredentials: true,
        headers: {
          'x-requested-with': 'XMLHttpRequest',
          'x-csrftoken': this.csrfToken
        }
        /*
        auth: {
          username: this.uname,
          password: this.passwd
        }
        */
      })
        .then(response => {
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteTask (id) {
      const path = `${apiUrl}/todolist/${id}/`
      axios.delete(path, {
        withCredentials: true,
        headers: {
          'x-requested-with': 'XMLHttpRequest',
          'x-csrftoken': this.csrfToken
        }
      })
        .then(response => {
          this.getFromBackend()
        })
        .catch(error => {
          console.log(error)
        })
    },
    editTask (task) {
      this.taskEditState = task.id
      console.log(this.taskEditState)
    },
    cancelEditTask () {
      this.taskEditState = null
    },
    doneEditTask (task) {
      this.taskEditState = null
      const path = `${apiUrl}/todolist/${task.id}/`
      axios.put(path, task, {
        withCredentials: true,
        headers: {
          'x-requested-with': 'XMLHttpRequest',
          'x-csrftoken': this.csrfToken
        }
      })
        .then(response => {
        })
        .catch(error => {
          console.log(error)
        })
    },
    addTask () {
      const path = `${apiUrl}/todolist/`
      axios.post(path, {'title': this.newTask}, {
        withCredentials: true,
        headers: {
          'x-requested-with': 'XMLHttpRequest',
          'x-csrftoken': this.csrfToken
        }
      })
        .then(response => {
          this.getFromBackend()
        })
        .catch(error => {
          console.log(error)
        })
    },
    login () {
      const path = `${apiUrl}/api-auth/login/`
      const fdata = new FormData()
      fdata.append('username', this.uname)
      fdata.append('password', this.passwd)
      fdata.append('csrfmiddlewaretoken', this.csrfToken)
      fdata.append('next', '/todolist/')
      axios({
        method: 'post',
        url: path,
        withCredentials: true,
        data: fdata,
        headers: {
          'x-requested-with': 'XMLHttpRequest',
          'x-csrftoken': this.csrfToken
        },
        validateStatus: (status) => {
          return status >= 200 && status < 303
        }
      })
        .then(response => {
          this.getFromBackend()
        })
        .catch(error => {
          console.log(error)
        })
    },
    logout () {
      const path = `${apiUrl}/api-auth/logout/`
      axios.get(path, {
        withCredentials: true
      })
        .then(response => {
          this.getFromBackend()
        })
        .catch(error => {
          console.log(error)
        })
    },
    setTestCookie () {
      const path = `${apiUrl}/cookietest/`
      axios.get(path, {}, {
        withCredentials: true
      })
        .then(response => {
        })
        .catch(error => {
          console.log(error)
        })
    },
    getCSRFToken () {
      const path = `${apiUrl}/csrf/`
      axios.get(path, {
        withCredentials: true
      })
        .then(response => {
          this.csrfToken = response.data.csrfToken
        })
        .catch(error => {
          console.log(error)
        })
    },
    getCurrentUser () {
      const path = `${apiUrl}/currentuser/`
      axios.get(path, {
        withCredentials: true
      })
        .then(response => {
          this.currentUser = response.data.username
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getFromBackend()
    this.getCSRFToken()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 0 10px;
  padding: 3px;
}
li.completed label {
  text-decoration: line-through;
}
.deletebtn, .editbtn {
  display: none;
  position: inherit;
}
li:hover .deletebtn {
  display: initial;
}
li:hover .editbtn {
  display: initial;
}
li.editing .tview {
  display: none;
}
li.editing .edit {
  display: inline;
}
a {
  color: #42b983;
}
.edit {
  position: relative;
}
li .edit {
  display: none;
}
</style>
