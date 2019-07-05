const API_ROOT = '/api'

const apiPeople = {
  people: '/people',
  peopleUpdate: '/people/update',
  snapshot: '/people/snapshot',
  snapshotUpdate: '/people/snapshot/update'
}

export const GetPeopleUri = API_ROOT.concat(apiPeople.people)
export const UpdatePeopleUri = API_ROOT.concat(apiPeople.peopleUpdate)
export const GetPeopleSnapshotUri = API_ROOT.concat(apiPeople.snapshot)
export const UpdatePeopleSnapshotUri = API_ROOT.concat(apiPeople.snapshotUpdate)
