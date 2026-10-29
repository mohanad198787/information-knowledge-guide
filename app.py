import streamlit as st
from datetime import date, timedelta
import json

st.set_page_config(page_title="المرشد الإرشادي للإطار العام للدراسة", page_icon="📚", layout="wide")
st.markdown("""<style>html,body,[class*="css"]{direction:rtl;text-align:right}.block-container{max-width:1150px}</style>""", unsafe_allow_html=True)
st.title("📚 المرشد الإرشادي لكتابة الإطار العام للدراسة")
st.subheader("قسم المعلومات وتقنيات المعرفة")
st.info("أداة إرشادية تفاعلية تعمل دون API للذكاء الاصطناعي. تساعدك على تنظيم أفكارك وبناء مسودة أولية، ولا تستبدل المشرف العلمي أو التحقق من المصادر.")

with st.sidebar:
    st.header("دليل الاستخدام")
    st.write("أجب عن المحاور ثم أنشئ المسودة ونزّلها للاحتفاظ بها.")
    st.caption("لا تحفظ هذه النسخة إجاباتك على خادم دائم. نزّل ملف JSON عند الحاجة.")

start = st.date_input("تاريخ بدء الاستخدام", value=date.today())
st.caption(f"فترة تنظيمية مقترحة لمدة 30 يوما: {start} إلى {start + timedelta(days=30)}. لا يوجد إيقاف تلقائي.")

st.header("أولا — معلومات الدراسة")
c1,c2=st.columns(2)
with c1:
    title=st.text_input("عنوان الدراسة")
    field=st.selectbox("المجال",["المعلومات وتقنيات المعرفة","إدارة مشاريع المعلومات","المكتبات ومؤسسات المعلومات","المصادر والخدمات الرقمية","إدارة المعرفة","المعلومات والذكاء الاصطناعي","مجال آخر"])
    institution=st.text_input("المؤسسة أو البيئة البحثية")
with c2:
    study_type=st.selectbox("نوع الدراسة",["وصفية","مسحية","تحليلية","تقويمية","دراسة حالة","ارتباطية","تجريبية أو شبه تجريبية","مختلطة","لم أحدد بعد"])
    population=st.text_input("مجتمع الدراسة")
    period=st.text_input("الفترة الزمنية")

st.header("ثانيا — عناصر الإطار العام")
with st.expander("١ — مشكلة الدراسة",expanded=True):
    problem=st.text_area("وصف المشكلة والظاهرة",height=100)
    gap=st.text_area("الفجوة البحثية أو الحاجة العملية",height=80)
    question=st.text_input("السؤال الرئيس")
    st.write("إرشاد: حدد ظاهرة قابلة للدراسة، ووثق الفجوة بمصادر موثوقة، ولا تفترض النتائج مسبقا.")
with st.expander("٢ — أهمية الدراسة"):
    imp_theory=st.text_area("الأهمية العلمية أو النظرية")
    imp_practice=st.text_area("الأهمية التطبيقية والجهات المستفيدة")
with st.expander("٣ — أهداف الدراسة"):
    objectives=st.text_area("كل هدف في سطر مستقل",height=110,placeholder="التعرف على...\nتحليل...\nتقويم...")
    st.caption("استخدم أفعالا قابلة للتحقق واربط الأهداف بالمشكلة.")
with st.expander("٤ — فرضيات الدراسة أو أسئلتها"):
    hyp_type=st.radio("التوجه المبدئي",["فرضيات قابلة للاختبار","أسئلة بحثية دون فرضيات","لم أحدد بعد"])
    hypotheses=st.text_area("الفرضيات أو الأسئلة الفرعية، كل واحدة في سطر")
    st.warning("ليست الفرضيات شرطا لكل دراسة. يعتمد القرار على سؤال الدراسة وتصميمها وطبيعة البيانات.")
with st.expander("٥ — حدود الدراسة"):
    limit_topic=st.text_input("الحدود الموضوعية")
    limit_place=st.text_input("الحدود المكانية")
    limit_time=st.text_input("الحدود الزمانية")
    limit_people=st.text_input("الحدود البشرية أو النوعية")
with st.expander("٦ — منهج الدراسة"):
    method=st.selectbox("المنهج المقترح",["المنهج الوصفي","المنهج المسحي","منهج دراسة الحالة","المنهج التحليلي","المنهج التاريخي","المنهج المقارن","المنهج التجريبي أو شبه التجريبي","المنهج المختلط","لم أحدد بعد"])
    method_reason=st.text_area("مبررات اختيار المنهج")
    st.caption("اختيار المنهج يعتمد على سؤال الدراسة ونوع الأدلة المطلوبة وليس على العنوان وحده.")
with st.expander("٧ — أدوات جمع البيانات"):
    tools=st.multiselect("الأدوات المحتملة",["الاستبانة","المقابلة","الملاحظة","تحليل المحتوى أو الوثائق","قائمة التدقيق","تحليل سجلات الاستخدام","مجموعات التركيز","اختبار أو مقياس","أداة أخرى"])
    tools_detail=st.text_area("كيف ستستخدم الأدوات ومن سيشارك؟")
    validity=st.text_area("الصدق والثبات أو موثوقية التحليل")
with st.expander("٨ — المعالجات الإحصائية أو التحليلية"):
    stats=st.multiselect("المعالجات المحتملة",["التكرارات والنسب المئوية","المتوسط الحسابي والانحراف المعياري","الوسيط والمدى","معامل الارتباط","اختبار ت للفروق","تحليل التباين","اختبارات لا معلمية","تحليل موضوعي نوعي","تحليل محتوى","تحليل مقارن","لم أحدد بعد"])
    stats_reason=st.text_area("مبررات اختيار المعالجات ونوع البيانات")
    st.caption("لا تعتمد اختبارا إحصائيا قبل تحديد نوع المتغيرات ومستوى القياس وافتراضات الاختبار.")
with st.expander("٩ — الدراسات السابقة"):
    previous=st.text_area("بيانات الدراسات ونتائجها الأساسية",height=130,placeholder="المؤلف والسنة والعنوان والهدف والمنهج والأداة والنتائج...")
    previous_gap=st.text_area("أوجه الاتفاق والاختلاف والفجوة")
    st.warning("لا يولد التطبيق مراجع ولا يتحقق من صحتها. راجع كل دراسة في مصدرها الأصلي.")
with st.expander("١٠ — التعريفات الإجرائية"):
    terms=st.text_area("المصطلحات الأساسية وتعريفها إجرائيا",height=110)
    st.caption("وضح كيف سيُفهم المصطلح أو يرصد أو يقاس داخل دراستك.")

checks=[]
for cond,msg in [
    (not title.strip(),"أدخل عنوان الدراسة"),
    (not problem.strip(),"اكتب وصف مشكلة الدراسة"),
    (not question.strip(),"حدد السؤال الرئيس"),
    (not objectives.strip(),"اكتب أهداف الدراسة"),
    (not limit_topic.strip(),"حدد الحدود الموضوعية"),
    (not limit_place.strip(),"حدد الحدود المكانية"),
    (method=="لم أحدد بعد","حدد المنهج بعد مراجعة المشكلة والأهداف"),
    (not tools,"حدد أدوات جمع البيانات"),
    (not previous.strip(),"أدخل الدراسات السابقة الموثقة"),
    (not terms.strip(),"اكتب التعريفات الإجرائية")]:
    if cond: checks.append(msg)
st.header("ثالثا — فحص أولي للاكتمال")
if checks:
    st.warning("نقاط تحتاج إلى استكمال")
    for x in checks: st.write("• "+x)
else:
    st.success("أدخلت العناصر الأساسية. راجع الاتساق بينها مع المشرف العلمي.")

def val(x): return x.strip() if isinstance(x,str) and x.strip() else "يستكمل لاحقا"
def lines(x):
    arr=[i.strip(" •-\t") for i in x.splitlines() if i.strip()]
    return "\n".join("- "+i for i in arr) if arr else "يستكمل لاحقا"

draft=f"""# الإطار العام للدراسة — مسودة أولية
## عنوان الدراسة
{val(title)}
## معلومات الدراسة
المجال: {field}
نوع الدراسة: {study_type}
المؤسسة: {val(institution)}
مجتمع الدراسة: {val(population)}
الفترة الزمنية: {val(period)}
## مشكلة الدراسة
{val(problem)}
الفجوة البحثية: {val(gap)}
السؤال الرئيس: {val(question)}
## أهمية الدراسة
الأهمية العلمية: {val(imp_theory)}
الأهمية التطبيقية: {val(imp_practice)}
## أهداف الدراسة
{lines(objectives)}
## فرضيات الدراسة أو أسئلتها
التوجه: {hyp_type}
{lines(hypotheses)}
## حدود الدراسة
الموضوعية: {val(limit_topic)}
المكانية: {val(limit_place)}
الزمانية: {val(limit_time)}
البشرية أو النوعية: {val(limit_people)}
## منهج الدراسة
المنهج: {method}
مبررات الاختيار: {val(method_reason)}
## أدوات جمع البيانات
الأدوات: {', '.join(tools) if tools else 'تحدد لاحقا'}
تفاصيل الاستخدام: {val(tools_detail)}
الصدق والثبات أو موثوقية التحليل: {val(validity)}
## المعالجات الإحصائية أو التحليلية
المعالجات: {', '.join(stats) if stats else 'تحدد لاحقا'}
المبررات: {val(stats_reason)}
## الدراسات السابقة
{val(previous)}
أوجه الإفادة والفجوة: {val(previous_gap)}
## التعريفات الإجرائية
{val(terms)}
## تنبيه
هذه مسودة أولية وليست صياغة نهائية. تحقق من المصادر وراجع اتساق المشكلة والأهداف والفرضيات والمنهج والأدوات مع المشرف العلمي.
"""
if st.button("إنشاء مسودة الإطار العام",type="primary",use_container_width=True):
    st.session_state["draft"]=draft
if "draft" in st.session_state:
    st.text_area("المسودة الأولية",st.session_state["draft"],height=450)
    st.download_button("تنزيل المسودة بصيغة Markdown",st.session_state["draft"],"مسودة_الإطار_العام.md","text/markdown")
    data={"title":title,"field":field,"study_type":study_type,"institution":institution,"population":population,"period":period,
          "problem":problem,"gap":gap,"question":question,"importance_theory":imp_theory,"importance_practice":imp_practice,
          "objectives":objectives,"hypothesis_type":hyp_type,"hypotheses":hypotheses,
          "limits":{"topic":limit_topic,"place":limit_place,"time":limit_time,"people":limit_people},
          "method":method,"method_reason":method_reason,"tools":tools,"tools_detail":tools_detail,"validity":validity,
          "stats":stats,"stats_reason":stats_reason,"previous_studies":previous,"previous_gap":previous_gap,"terms":terms}
    st.download_button("تنزيل إجاباتك بصيغة JSON",json.dumps(data,ensure_ascii=False,indent=2),"إجابات_الدراسة.json","application/json")
st.divider()
st.caption("نسخة إرشادية لقسم المعلومات وتقنيات المعرفة. لا تستخدم نموذجا لغويا خارجيا ولا ترسل إجاباتك إلى خدمة ذكاء اصطناعي. إذا نشرت التطبيق سحابيا فسيعمل على خادم الاستضافة.")
