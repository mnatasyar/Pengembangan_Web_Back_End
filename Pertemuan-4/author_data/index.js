import AuthorData from './author_data.js';
let authordata = new AuthorData()
let show = function(){
    console.log(authordata)
    authordata.getProfile().then(data=>{
        authordata.showProfile(data);
    }).catch(e => console.log(e));
}
show();