import axios from 'axios'
import {PeopleResource} from './resource'

export default {
  getParentLoginResource () {
    return axios.post(PeopleResource)
  }
}
