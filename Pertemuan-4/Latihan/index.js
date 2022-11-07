import AuthorData from './author_data.js';

let authorData = new AuthorData()

let show = function() {
    console.log(authorData);
    authorData.getProfile().then(data => {
        authorData.showProfile(data)
    }).catch(e => console.log(e))
}
show()