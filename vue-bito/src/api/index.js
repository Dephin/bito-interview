import axios from 'axios'
import {PeopleResource} from './resource'

export default {
  getParentResource () {
    return axios.post(PeopleResource)
  }
}
