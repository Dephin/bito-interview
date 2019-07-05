import axios from 'axios'
import {GetPeopleUri, UpdatePeopleUri, GetPeopleSnapshotUri, UpdatePeopleSnapshotUri} from './resource'

export default {
  getPeopleResource () {
    return axios.get(GetPeopleUri)
  },
  updatePeopleResource (data) {
    return axios.post(UpdatePeopleUri, data)
  },
  getPeopleSnapshotResource (limit) {
    return axios.post(GetPeopleSnapshotUri, {
      params: {
        limit: limit
      }
    })
  },
  updatePeopleSnapshotResource (data) {
    return axios.post(UpdatePeopleSnapshotUri, data)
  }
}
