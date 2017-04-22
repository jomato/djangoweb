KindEditor.ready(function (K){
	window.editor = K.create('textarea[name="content"]',{
		width:'200',
		heigth:'200',
		uploadJson:'/admin/upload/'

	});
});