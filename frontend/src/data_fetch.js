const host_name = 'idk ryan\'s ip, will find later'

export default get_something = (setData) => fetch(host_name+'/get_')
.then(response => setData(response.json()))

