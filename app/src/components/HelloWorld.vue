<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <label for="input-item">Title</label>
    <input type="text" name="input-item" v-model="title" >
    <div v-if="suggestions">
      <ul>
        <li v-for="(item,index) in suggestions" :key="index">
          {{ index }}. Title: {{ item.title }},
          <br />
          Confidence: {{ item.confidence }}
        </li>
      </ul>
    </div>
    <div v-if="error">{{ error }}</div>
    <button @click="search">Search</button>
    <button @click="reset">Reset</button>

  </div>
</template>

<script>
import axios from "axios"
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      title: '',
      suggestions: [],
      error: ''
    }
  },
  
methods: {
    search() {
      const options = {
        headers: {'Content-Type': 'application/json'}
      };

      axios.post('http://127.0.0.1:5000/api/', {
        title: this.title
      }, options).then((res) => {
        this.suggestions = res.data.result
        console.log(this.suggestions)
      }).catch((err) => {
        this.error = err
      })
    },
    check(title) {
      console.log(title)
    },
    reset() {
      this.title = '',
      this.suggestions = [],
      this.error = ''
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
