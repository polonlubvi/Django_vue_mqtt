<template>
  <div class="hello">
    <h1 class="title">Task</h1> <!-- Page title -->

    <hr>

    <div class="columns">
      <div class="colum is-one-third is-offset-one-third"> <!-- Narrow center column -->
        <form><!-- Form for adding tasks -->
          <h2 class="subtitle">Add task</h2>

          <div class="field"> <!-- Mormal input field for the description -->
            <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text">
            </div>
          </div>

          <div class="field"> <!-- Select field for choosing the status (0 and 1 as value, same as in the django status choices) -->
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select>
                  <option value="0">To do</option>
                  <option value="1">Done</option>
                </select>
              </div>
            </div>
          </div>


          <div class="field is-grouped"> <!-- Submit button -->
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <hr>

    <div class="columns">
      <div class="columns is-half"> <!-- Half of the column for todo task -->
        <h2 class="subtitle">Todo</h2>

        <div class="todo">
          <div class="card" v-if="task.status == 0"> <!-- Loop through the tasks array, if status is 0 (to do) then we'll show it. -->
            <div class="card-content"  v-for="task in tasks" v-bind:key="task">
              <div class="content">
                {{ task.description }} <!-- Print the task's description here -->
              </div>
            </div>

            <footer class="card-footer">
              <a class="card-footer-item">Done</a> <!-- Button fot setting a tasl to done -->
            </footer>
          </div>
        </div>
      </div>

      <div class="column is-half"> <!-- Half of the column for done tasks -->
        <h2 class="subtitle">Done</h2>

        <div class="done">
          <div class="card" v-if="task.status == 1">
            <div class="card-content"  v-for="task in tasks" v-bind:key="task">
              <div class="content">
                {{ task.description }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      tasks: [] // Array for holding the tasks

    }
  },
  mounted () { // This will be called when HelloWorld is loaded
    this.getTasks(); // Call our gerTasks function below

  },
  methods: {
    getTasks() {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/tasks/',
        auth:{
          username: 'admin',
          password: 'password1200'
        }
      }).then(response => this.tasks = response.data);
    }
  }
}
</script>

<style scoped>

.select, select {/* 100% width for the select */
  width: 100%;
}

.card { /* Adding some air under the tasds */
  margin-bottom: 25px;
}

.done { /* Make the done taska a little bit transparent */
opacity: 0.3;
}

</style>

