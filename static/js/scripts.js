$('.box-plus').click(function(){
	id = $(this).parent().find('.box-id').val();
	$('#box_id').val(id);
});

$('.box-close').click(function(){
	id = $(this).parent().find('.box-id').val();
	$('#delete_box_id').val(id);
})