import axios from 'axios'

export const share1 = newReq => {
    return axios.post('shares/share1', {
        student_id:newReq.student_id,    
        hashes: newReq.hashes,
			name: newReq.name,
            
        }).then(res => {
            console.log('Done!')
        })
}


//export const num = numbers =>{
//    var number = 0;
//    number =  numbers
//    return number
//}