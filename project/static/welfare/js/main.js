/********* 교육과정 팝업 ************/
                $(function(){
                    $(".cclum_btn.ccm").click(function(){
                        $(".pop_bg").fadeIn();
                        $(".cclum_popup.ccm").fadeIn();
                    });
                    $(".cclum_btn.degree").click(function(){
                        $(".pop_bg").fadeIn();
                        $(".cclum_popup.degree").fadeIn();
                    });
                    $(".cclum_popup .close").click(function(){
                        $(".pop_bg").hide();
                        $(".cclum_popup").hide();
                    });
                    $(".pop_bg").click(function(){
                        $(".pop_bg").hide();
                        $(".cclum_popup").hide();
                    });
                });

/********* 커리큘럼 탭 ************/


                // 요소 선택
                const curriculumTabs = document.querySelectorAll('#curriculum_tab a');
                const curriculumContents = document.querySelectorAll('#curriculum_contents ul');
                const curriculumLinks = document.querySelectorAll('#curriculum_cate_ul_field_01 a');
                const curriculumLinks01 = document.querySelectorAll('#curriculum_cate_ul_field_02 a');
                const curriculumLinksall = document.querySelectorAll('#curriculum_contents ul a');
                const txt01 = document.querySelector('.txt01');
                const txt02 = document.querySelector('.txt02');
                const curriculum_list = document.querySelectorAll('.curriculum_list ul li');
             
             
               // 각 링크에 대한 이벤트 리스너 등록
                curriculumTabs.forEach(tab => {
                   tab.addEventListener('click', function(e) {
                      e.preventDefault();
             
                      // 다른 탭의 'active' 클래스 제거
                      curriculumTabs.forEach(otherTab => otherTab.classList.remove('active'));
                      // 클릭된 탭에 'active' 클래스 추가
                      this.classList.add('active');
                      // 모든 컨텐츠 숨기기
                      curriculumContents.forEach(content => content.classList.add('hidden'));
                      // 클릭된 탭에 해당하는 컨텐츠만 표시
                      const fieldToShow = document.querySelector(`#curriculum_cate_ul_${this.getAttribute('data-field')}`);
                      if (fieldToShow) {
                         fieldToShow.classList.remove('hidden');
                      }
                      // 텍스트 업데이트
                      const txtField = this.getAttribute('data-field');
                      if (txtField === 'field_01') {
                         txt01.textContent = '사회복지';
                         txt02.textContent = document.querySelector('.field_01 .active').textContent;
                      } else if (txtField === 'field_02') {
                         txt01.textContent = '심리상담';
                         txt02.textContent = document.querySelector('.field_02 .active').textContent;
                      }
                   });
                });
             
                 document.addEventListener("DOMContentLoaded", function() {
             
                     document.querySelector('[data-field="field_01"]').addEventListener("click", function() {
                         document.querySelector('.curriculum_list_01').style.display = "flex";
                         document.querySelector('.curriculum_list_02').style.display = "none";
                     });
             
             
                     document.querySelector('[data-field="field_02"]').addEventListener("click", function() {
                         document.querySelector('.curriculum_list_02').style.display = "flex";
                         document.querySelector('.curriculum_list_01').style.display = "none";
                     });
                 });
             
                // 각 링크에 대한 이벤트 리스너 등록
                curriculumLinks.forEach(link => {
                   link.addEventListener('click', function(e) {
                      e.preventDefault();
             
                      // 다른 링크의 'active' 클래스 제거
                      curriculumLinks.forEach(otherLink => otherLink.classList.remove('active'));
                      // 클릭된 링크에 'active' 클래스 추가
                      this.classList.add('active');
             
                      // 텍스트 업데이트
                      txt02.textContent = this.textContent;
                   });
                });
             
                // 각 링크에 대한 이벤트 리스너 등록
                curriculumLinks01.forEach(link => {
                   link.addEventListener('click', function(e) {
                      e.preventDefault();
             
                      // 다른 링크의 'active' 클래스 제거
                      curriculumLinks01.forEach(otherLink => otherLink.classList.remove('active'));
                      // 클릭된 링크에 'active' 클래스 추가
                      this.classList.add('active');
             
                      // 텍스트 업데이트
                      txt02.textContent = this.textContent;
                   });
                });
               
                 curriculumTabs.forEach(tab => {
                     tab.addEventListener('click', function(e) {
                         e.preventDefault();
             
                         // 모든 탭에서 'active' 클래스 제거
                         curriculum_list.forEach(otherTab => otherTab.classList.remove('active'));
                         
                         // 현재 클릭한 탭에만 'active' 클래스 추가
                         this.classList.add('active');
                     });
                 });
             
          $(function(){         
                // 초기값 설정
                txt01.textContent = '사회복지';
                txt02.textContent = document.querySelector('.field_01 .active').textContent;
             

            });                


/********* 자격증 슬라이드 ************/
            $(function(){

                var mySwiper = new Swiper ('.certifi_swiper .swiper-container', {
                    speed: 400,
                    spaceBetween: 20,
                    slidesPerView: 1,
                    centeredSlides: true,
                    loop: true,
                    autoplay: {
                        delay: 3000,
                    },
                    pagination : {
                        el : '.certifi_swiper .swiper-pagination', 
                        clickable : true,
                        type : 'bullets',
                    },
                    breakpoints: {  
                        650: {
                            slidesPerView: 2,
                            spaceBetween: 30,
                        },
                        1200: {
                            slidesPerView: 3,
                            spaceBetween: 60,
                        },
                    },          
                });
            });


/********* 교수소개 ************/
                $(function(){
                    $('.pf_list li').click(function(){
                        // 현재 클릭한 li 요소에 .on 클래스를 추가하고 형제 요소의 .on 클래스를 제거합니다.
                        $(this).toggleClass('on').siblings().removeClass('on');
                    });
                });


/********* 협력기관 ************/
            $(function(){
                var mySwiper = new Swiper ('.partner_swiper .swiper-container', {
                    speed: 400,
                    spaceBetween: 20,
                    slidesPerView: 2,
                    loop: true,
                    autoplay: {
                        delay: 3000,
                        disableOnInteraction: false,
                    },
                    breakpoints: {  
                        550: {
                        slidesPerView: 3, 
                        spaceBetween: 20,
                        },
                        768: {
                        slidesPerView: 4, 
                        spaceBetween: 20,
                        },
                        1020: {
                        slidesPerView: 5, 
                        spaceBetween: 20,
                        },
                        1400: {
                        slidesPerView: 6,
                        spaceBetween: 20,
                        },
                    },     
                });
                });

