$(function(){
    // best hotel 탭클릭
    $(".main_page ul.main_slide_tab.best li").click(function(){
        let i = $(this).index();
        $(".main_page ul.main_slide_tab.best li").removeClass("on").eq(i).addClass("on");
        $(".main_page ul.show_slide li").removeClass("on").eq(i).addClass("on");
    });
    // 패키지 탭 클릭
    $(".main_page ul.main_slide_tab.pakage_tab li").click(function(){
        let i = $(this).index();
        $(".main_page ul.main_slide_tab.pakage_tab li").removeClass("on").eq(i).addClass("on");
        $(".main_page ul.show_slide02 li").removeClass("on").eq(i).addClass("on");
        $(".pakage .show_link li").removeClass("on").eq(i).addClass("on");
    });


    
});