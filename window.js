function topLevel(t="Toplevel"){
  const o=document.createElement('div');
  o.style.cssText='position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.3);z-index:9999;display:flex;justify-content:center;align-items:center';
  const w=document.createElement('div');
  w.className='w';
  w.style.cssText='background:#fff;border-radius:8px;box-shadow:0 10px 40px rgba(0,0,0,.3);width:500px;max-width:90vw;padding:0 20px 20px;position:relative;font-family:sans-serif';
  const h=document.createElement('div');
  h.style.cssText='display:flex;justify-content:space-between;align-items:center;font-weight:bold;font-size:18px;padding:12px 0;cursor:move;user-select:none;border-bottom:1px solid #eee;margin-bottom:12px';
  h.textContent=t;
  const b=document.createElement('div');
  b.style.cssText='min-height:100px';
  w.appendChild(h);
  w.appendChild(b);
  o.appendChild(w);
  document.body.appendChild(o);
  let d=false,e,f;
  h.onmousedown=(m)=>{
    d=true;
    e=m.clientX-w.getBoundingClientRect().left;
    f=m.clientY-w.getBoundingClientRect().top;
    document.onmousemove=(n)=>{
      if(!d)return;
      w.style.left=(n.clientX-e)+'px';
      w.style.top=(n.clientY-f)+'px';
      w.style.position='fixed';
    };
    document.onmouseup=()=>{d=false;document.onmousemove=null;document.onmouseup=null};
  };
  const r=()=>{w.classList.add('x');setTimeout(()=>o.remove(),200)};
  return {body:b,overlay:o,win:w,close:r};
}
