ArticlesList = new Mongo.Collection('articles');


Template.layout.articles =function(){
  Meteor.call('getArticles',function(err,results){
  Session.set('article',JSON.parse(results.content));
  });
  var Article = Session.get('article');
    return (Article);
};



Template.addSearchForm.events({
  'submit form': function(event){
    event.DefaultPrevented();
    var TitleVar = event.target.Title.value;
    console.log(TitleVar);
    var Article = Session.get('article');
    for (i=0;i<Article.length;i++){
      var data = Article[i].title;
      if(TitleVar == data){
         document.write(TitleVar);      
      }
   }
   
 }
});

