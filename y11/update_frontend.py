import re

with open('static/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Tag Color & Label
text = text.replace("building_parts:'#9B51E0'", "building_parts:'#0D9488'")
text = text.replace("s.type.replace('_',' ')}</div>", "s.type==='building_parts'?'principal parts':s.type.replace('_',' ')}</div>")

# 2. Menu Button position fix
text = text.replace(
    "style={{position:'fixed',top:16,right:20,zIndex:50",
    "style={{position:'fixed',top:24,right:40,zIndex:50"
)

# 3. BPFC & TranslateForm duplicate menu btn cleanup
text = text.replace('<button className="menu-btn" onClick={onDone}>← Menu</button>', '')

# 4. Flashcard sizing fix
text = text.replace(".part-chip{font-family:'Crimson Text',serif;font-style:italic;font-size:1.7rem;font-weight:700;color:var(--dark);background:var(--white);border:2px solid var(--lgrey);border-radius:14px;padding:16px 28px}", ".part-chip{font-family:'Crimson Text',serif;font-style:italic;font-size:1.7rem;font-weight:700;color:var(--dark);background:var(--white);border:2px solid var(--lgrey);border-radius:14px;padding:16px 28px;white-space:nowrap;min-width:120px}")

# 5. TypedBase Feedback cleanup
tb_old = """              {retype&&<div className="anim-fade" style={{marginTop:30,width:'100%',maxWidth:800}}>
                <div style={{background:'var(--gold)',color:'white',padding:'12px 20px',borderRadius:12,fontWeight:800,marginBottom:16,fontSize:'1.05rem'}}>You got this wrong — you'll see it again at the end of the set.</div>
                <div className="feedback bad" style={{marginBottom:20}}>{renderText(fb.message)}</div>
                <p style={{fontSize:'1.2rem',marginBottom:12,fontWeight:800,color:'var(--navy)'}}>Now type the correct answer:</p>
                <div style={{marginBottom:20,padding:'16px 20px',background:'#f0fdf4',border:'2px solid #16a34a',borderRadius:12,textAlign:'left'}}><p style={{fontWeight:700,fontSize:'0.85rem',color:'#16a34a',marginBottom:6,textTransform:'uppercase',letterSpacing:'0.05em'}}>Correct answer</p><p className={isLatin?'latin':''} style={{fontSize:'1.3rem',fontWeight:800,color:'var(--dark)'}}>{correct}</p></div>"""
tb_new = """              {retype&&<div className="anim-fade" style={{marginTop:16,width:'100%',maxWidth:800,padding:'24px',background:'var(--white)',border:'3px solid var(--red-bright)',borderRadius:20}}>
                <div style={{background:'var(--gold)',color:'white',padding:'8px 16px',borderRadius:10,fontWeight:800,marginBottom:20,display:'inline-block'}}>You'll see this again at the end</div>
                <div style={{marginBottom:24,padding:'20px',background:'#f0fdf4',border:'2px solid #16a34a',borderRadius:16,textAlign:'left'}}><p style={{fontWeight:800,fontSize:'0.9rem',color:'#16a34a',marginBottom:8,textTransform:'uppercase',letterSpacing:'0.05em'}}>The Answer Was</p><p className={isLatin?'latin':''} style={{fontSize:'1.8rem',fontWeight:800,color:'var(--dark)'}}>{correct}</p></div>
                <p style={{fontSize:'1.2rem',marginBottom:12,fontWeight:800,color:'var(--navy)'}}>Type it to continue:</p>"""
text = text.replace(tb_old, tb_new)

# 6. BPTyped Feedback cleanup
bp_old = """              {retype&&<div className="anim-fade" style={{marginTop:20,width:'100%',maxWidth:800}}>
                <div style={{background:'var(--gold)',color:'white',padding:'12px 20px',borderRadius:12,fontWeight:800,marginBottom:16}}>You got this wrong — you'll see it again at the end of the set.</div>
                <p style={{color:'var(--grey)',marginBottom:12,fontWeight:700}}>The correct answer is <span className="latin" style={{color:'var(--navy)',fontWeight:800}}>{correct}</span>. Now type it:</p>"""
bp_new = """              {retype&&<div className="anim-fade" style={{marginTop:16,width:'100%',maxWidth:800,padding:'24px',background:'var(--white)',border:'3px solid var(--red-bright)',borderRadius:20}}>
                <div style={{background:'var(--gold)',color:'white',padding:'8px 16px',borderRadius:10,fontWeight:800,marginBottom:20,display:'inline-block'}}>You'll see this again at the end</div>
                <div style={{marginBottom:24,padding:'20px',background:'#f0fdf4',border:'2px solid #16a34a',borderRadius:16,textAlign:'left'}}><p style={{fontWeight:800,fontSize:'0.9rem',color:'#16a34a',marginBottom:8,textTransform:'uppercase',letterSpacing:'0.05em'}}>The Answer Was</p><p className="latin" style={{fontSize:'1.8rem',fontWeight:800,color:'var(--dark)'}}>{correct}</p></div>
                <p style={{fontSize:'1.2rem',marginBottom:12,fontWeight:800,color:'var(--navy)'}}>Type it to continue:</p>"""
text = text.replace(bp_old, bp_new)

# 7. Sentences Feedback cleanup
sent_old = """              {retype&&<div className="anim-fade" style={{marginTop:20,width:'100%',maxWidth:900}}>
                <div style={{background:'var(--gold)',color:'white',padding:'12px 20px',borderRadius:12,fontWeight:800,marginBottom:16}}>You got this wrong — you'll see it again at the end of the set.</div>
                <p style={{color:'var(--grey)',marginBottom:12,fontWeight:700}}>The answer is: <strong style={{color:'var(--navy)'}}>{fb.correct_answer}</strong>. Now type it:</p>"""
sent_new = """              {retype&&<div className="anim-fade" style={{marginTop:16,width:'100%',maxWidth:900,padding:'24px',background:'var(--white)',border:'3px solid var(--red-bright)',borderRadius:20}}>
                <div style={{background:'var(--gold)',color:'white',padding:'8px 16px',borderRadius:10,fontWeight:800,marginBottom:20,display:'inline-block'}}>You'll see this again at the end</div>
                <div style={{marginBottom:24,padding:'20px',background:'#f0fdf4',border:'2px solid #16a34a',borderRadius:16,textAlign:'left'}}><p style={{fontWeight:800,fontSize:'0.9rem',color:'#16a34a',marginBottom:8,textTransform:'uppercase',letterSpacing:'0.05em'}}>The Answer Was</p><p style={{fontSize:'1.5rem',fontWeight:800,color:'var(--dark)'}}>{fb.correct_answer}</p></div>
                <p style={{fontSize:'1.2rem',marginBottom:12,fontWeight:800,color:'var(--navy)'}}>Type it to continue:</p>"""
text = text.replace(sent_old, sent_new)

# 8. FullParsing refactor
parse_old = """    const PERSONS=['1st','2nd','3rd'];
    const NUMBERS=['singular','plural'];
    const [idx,setIdx]=useState(0);
    const [selTense,setSelTense]=useState(null);
    const [selPerson,setSelPerson]=useState(null);
    const [selNumber,setSelNumber]=useState(null);"""

parse_new = """    const PERSON_NUMBERS=[
        {id:'1-s',label:'I',p:'1st',n:'singular'},{id:'2-s',label:'you',p:'2nd',n:'singular'},{id:'3-s',label:'he/she/it',p:'3rd',n:'singular'},
        {id:'1-p',label:'we',p:'1st',n:'plural'},{id:'2-p',label:'you (pl.)',p:'2nd',n:'plural'},{id:'3-p',label:'they',p:'3rd',n:'plural'}
    ];
    const [idx,setIdx]=useState(0);
    const [selTense,setSelTense]=useState(null);
    const [selPerson,setSelPerson]=useState(null);
    const [selNumber,setSelNumber]=useState(null);
    const selPN = (selPerson && selNumber) ? `${selPerson}-${selNumber}`.substring(0,3) : null;"""
text = text.replace(parse_old, parse_new)

parse_buttons_old = """            <BtnGroup label="Tense" options={TENSES} selected={selTense} onSelect={setSelTense}/>
            <BtnGroup label="Person" options={PERSONS} selected={selPerson} onSelect={setSelPerson}/>
            <BtnGroup label="Number" options={NUMBERS} selected={selNumber} onSelect={setSelNumber}/>"""

parse_buttons_new = """            <BtnGroup label="Tense" options={TENSES} selected={selTense} onSelect={setSelTense}/>
            <div style={{marginBottom:20}}>
              <p style={{fontWeight:800,color:'var(--grey)',fontSize:'0.85rem',textTransform:'uppercase',letterSpacing:'0.08em',marginBottom:8}}>Person / Number</p>
              <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:10}}>
                {PERSON_NUMBERS.map(pn=><button key={pn.id} disabled={!!fb}
                  onClick={()=>{if(pn.id===selPN){setSelPerson(null);setSelNumber(null)}else{setSelPerson(pn.p);setSelNumber(pn.n)}}}
                  style={{padding:'14px 10px',borderRadius:12,border:`2px solid ${pn.id===selPN?'var(--navy)':'var(--lgrey)'}`,
                    background:pn.id===selPN?'var(--navy)':'var(--white)',color:pn.id===selPN?'var(--white)':'var(--dark)',
                    fontWeight:700,fontSize:'1.1rem',cursor:fb?'default':'pointer',transition:'all .15s'}}>
                  {pn.label}
                </button>)}
              </div>
            </div>"""
text = text.replace(parse_buttons_old, parse_buttons_new)

# Eliminate em-dashes globally
text = text.replace("—", "-")

with open('static/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html formatting, styles, parsing logic and feedback structures.")
