Meteor.methods({
'getArticles':function(){
 var result = Meteor.http.call('GET','http://127.0.0.1:8000/api/v1/blog_collection');
 return result;
}
});






