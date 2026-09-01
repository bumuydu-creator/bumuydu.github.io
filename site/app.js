(() => {
  const video=document.querySelector('#heroVideo'), cinema=document.querySelector('#cinema'), copy=document.querySelector('.scene-copy'), title=document.querySelector('.scene-title'), body=document.querySelector('.scene-body'), counter=document.querySelector('.scene-counter'), timeReadout=document.querySelector('#timeReadout'), progressReadout=document.querySelector('.progress-readout');
  const scenes=[
    {at:0,title:'Hikâye,<br><em>görüntüden önce</em><br>başlar.',body:'Bazen bir masalın ilk hatırladığımız şeyi olay değil, görüntüdür.'},
    {at:.22,title:'Ormanın içinde<br>bir <em>hafıza</em><br>hareket eder.',body:'Yaprakların arasından geçen figür, anlatının kendisinden önce gelir.'},
    {at:.47,title:'Kırmızı,<br><em>tanıdık</em> bir<br>işarettir.',body:'Bir renk, bir karakteri çağırabilir. Bir görüntü, bütün bir masalı.'},
    {at:.76,title:'Ve masal,<br><em>yeniden</em><br>hatırlanır.',body:'Eski görüntü kaybolmaz; her bakışta başka bir biçime dönüşür.'}
  ];
  let duration=0,targetTime=0,displayedTime=0,lastScene=-1,raf=0;
  const clamp=(n,a,b)=>Math.max(a,Math.min(b,n)),lerp=(a,b,t)=>a+(b-a)*t;
  const getProgress=()=>{const r=cinema.getBoundingClientRect(),max=cinema.offsetHeight-innerHeight;return clamp(-r.top/max,0,1)};
  const sceneFor=p=>{let i=0;scenes.forEach((s,j)=>{if(p>=s.at)i=j});return i};
  function renderScene(i){if(i===lastScene)return;lastScene=i;const s=scenes[i];title.innerHTML=s.title;body.textContent=s.body;counter.textContent=`${String(i+1).padStart(2,'0')} / ${String(scenes.length).padStart(2,'0')}`;copy.animate([{opacity:.15,transform:'translateY(-48%) translateY(16px)'},{opacity:1,transform:'translateY(-50%) translateY(0)'}],{duration:650,easing:'cubic-bezier(.16,1,.3,1)',fill:'both'})}
  function tick(){displayedTime=lerp(displayedTime,targetTime,.12);if(video.readyState>=2&&Math.abs(video.currentTime-displayedTime)>.015){try{video.currentTime=displayedTime}catch(e){}}const p=duration?displayedTime/duration:0;timeReadout.textContent=`00:${String(Math.min(59,Math.floor(displayedTime))).padStart(2,'0')}`;progressReadout.textContent=`${String(Math.round(p*100)).padStart(2,'0')}%`;renderScene(sceneFor(p));raf=requestAnimationFrame(tick)}
  video.addEventListener('loadedmetadata',()=>{duration=video.duration||5.04;video.currentTime=0;displayedTime=0;targetTime=0;raf=requestAnimationFrame(tick)},{once:true});
  addEventListener('scroll',()=>{targetTime=duration*getProgress()},{passive:true});
  addEventListener('resize',()=>{targetTime=duration*getProgress()});
  document.querySelector('.scroll-cue')?.addEventListener('click',()=>scrollTo({top:cinema.offsetTop+innerHeight*.35,behavior:'smooth'}));
  addEventListener('beforeunload',()=>cancelAnimationFrame(raf));
})();
