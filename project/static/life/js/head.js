/********** 모바일 상단 메뉴 ******************/
$(function() {

	$('.mobile-list .gnb_1da').click(function(e) {
		e.stopPropagation(); // 메뉴를 열고 닫을 때 이벤트 전파 방지

		if (!$(this).hasClass('on')) {
			$(this).addClass('on');
		} else {
			$(this).removeClass('on');
		}

		$(this).next('.mb-sub-ul').slideToggle(); // 다음에 오는 ul 요소를 찾아 슬라이드 토글

		return false; // 기본 이벤트 방지 (링크로의 이동 등)
	});

	$('.mobile-menu > ul > li:not(:last-child)').click(function() {
		$(this).find('.gnb_1da').trigger('click'); // 메뉴 항목을 클릭하면 하위 메뉴가 열리도록 트리거
	});

	$('.mobile-list .gnb_1da').bind('touchstart', function(e) {
		$(this).trigger('click');
		e.preventDefault();
	});

	$('.mobile-list:last-child .gnb_1da').click(function(e) {
		e.stopPropagation(); // 이벤트 전파 방지
		window.open($(this).attr('href'), '_blank'); // "대학홈페이지"를 클릭하면 새 창에서 열림
	});

	$(".btn_mob_button").click(function() {
		$("#aside").animate({
			"right": "0px"
		}, 200);
		$(".mask").css('display', 'block');
		$("#aside").css('display', 'block');
		$(".close_menu").animate({
			"right": "20px"
		}, 200);
		$("body").css("position", "fixed");
		$(".foot_logo").animate({
			"right": "auto",
			"left": "20px"
		}, 200);
	});

	$("#mobile_menu_close, .mask").click(function() {
		$("#aside").animate({
			"right": "-100%"
		}, 200);
		$(".close_menu").animate({
			"right": "-100%"
		}, 200);
		$(".mask").css('display', 'none');
		$("#aside").css('display', 'none');
		$("body").css("position", "relative");
		$(".foot_logo").animate({
			"left": "120%",
			"right": "-100%"
		}, 200);
	});

});
