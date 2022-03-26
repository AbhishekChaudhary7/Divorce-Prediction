import streamlit as st
import pickle
import numpy as np
import time

@st.cache(allow_output_mutation=True)
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)

    return data


data = load_model()

model = data['model']
#Q1 = data['Q1']
#Q2 = data['Q2']

def show_predict_page():
    st.markdown("![Alt Text](https://media.giphy.com/media/fv8KclrYGp5dK/giphy.gif)")
    st.title("Divorce Detection// by_dKC")
    st.write("""### Go through the questionnaire to predict your divorce""")
    st.write("""##### _Answer your quesions 0 being the lowest and 4 being the highest._""")

    Q1 = st.slider('Q1. If one of us apologizes when our discussion deteriorates, the discussion ends.', 0,4)
    Q2 = st.slider('Q2. I know we can ignore our differences, even if things get hard sometimes.',0,4)
    Q3 = st.slider('Q3. When we need it, we can take our discussions with my spouse from the beginning and correct it.',0,4)
    Q4 = st.slider('Q4. When I discuss with my spouse, to contact him will eventually work.',0,4)
    Q5 = st.slider('Q5. The time I spent with my wife is special for us.',0,4)
    Q6 = st.slider('Q6. We dont have time at home as partners.',0,4)
    Q7 = st.slider('Q7. We are like two strangers who share the same environment at home rather than family.',0,4)
    Q8 = st.slider('Q8. I enjoy our holidays with my wife.',0,4)
    Q9 = st.slider('Q9. I enjoy traveling with my wife.',0,4)
    Q10 = st.slider('Q10. Most of our goals are common to my spouse.',0,4)
    Q11 = st.slider('Q11. I think that one day in the future, when I look back, I see that my spouse and I have been in harmony with each other.',0,4)
    Q12 = st.slider('Q12. My spouse and I have similar values in terms of personal freedom.',0,4,)
    Q13 = st.slider('Q13. My spouse and I have similar sense of entertainment.',0,4,)
    Q14 = st.slider('Q14. Most of our goals for people (children, friends, etc.) are the same.',0,4,)
    Q15 = st.slider('Q15. Our dreams with my spouse are similar and harmonious.',0,4,)
    Q16 = st.slider('Q16. We are compatible with my spouse about what love should be.',0,4,)
    Q17 = st.slider('Q17. We share the same views about being happy in our life with my spouse',0,4,)
    Q18 = st.slider('Q18. My spouse and I have similar ideas about how marriage should be',0,4,)
    Q19 = st.slider('Q19. My spouse and I have similar ideas about how roles should be in marriage',0,4,)
    Q20 = st.slider('Q20. My spouse and I have similar values in trust.',0,4,)
    Q21 = st.slider('Q21. I know exactly what my wife likes.',0,4,)
    Q22 = st.slider('Q22. I know how my spouse wants to be taken care of when she/he sick.',0,4,)
    Q23 = st.slider('Q23. I know my spouses favorite food.',0,4,)
    Q24 = st.slider('Q24. I can tell you what kind of stress my spouse is facing in her/his life.',0,4,)
    Q25 = st.slider('Q25. I have knowledge of my spouses inner world.',0,4,)
    Q26 = st.slider('Q26. I know my spouses basic anxieties.',0,4,)
    Q27 = st.slider('27. I know what my spouses current sources of stress are.',0,4,)
    Q28 = st.slider('Q28. I know my spouses hopes and wishes.',0,4,)
    Q29 = st.slider('Q29. I know my spouse very well.',0,4,)
    Q30 = st.slider('Q30. I know my spouses friends and their social relationships.',0,4,)
    Q31 = st.slider('Q31. I feel aggressive when I argue with my spouse.',0,4,)
    Q32 = st.slider('Q32. When discussing with my spouse, I usually use expressions such as ‘you always’ or ‘you never’ .',0,4,)
    Q33 = st.slider('Q33. I can use negative statements about my spouses personality during our discussions.',0,4,)
    Q34 = st.slider('Q34. I can use offensive expressions during our discussions.',0,4,)
    Q35 = st.slider('Q35. I can insult my spouse during our discussions.',0,4,)
    Q36 = st.slider('Q36. I can be humiliating when we discussions.',0,4,)
    Q37 = st.slider('Q37. My discussion with my spouse is not calm',0,4,)
    Q38 = st.slider('Q38. I hate my spouses way of open a subject.',0,4,)
    Q39 = st.slider('Q39. Our discussions often occur suddenly.',0,4,)
    Q40 = st.slider('Q40. We are just starting a discussion before I know what is going on.',0,4,)
    Q41 = st.slider('Q41. When I talk to my spouse about something, my calm suddenly breaks.',0,4,)
    Q42 = st.slider('Q42. When I argue with my spouse, i only go out and I dont say a word.',0,4,)
    Q43 = st.slider('Q43. I mostly stay silent to calm the environment a little bit.',0,4,)
    Q44 = st.slider('Q44. Sometimes I think it is good for me to leave home for a while.',0,4,)
    Q45 = st.slider('Q45. I would rather stay silent than discuss with my spouse.',0,4,)
    Q46 = st.slider('Q46. Even if I am right in the discussion, I stay silent to hurt my spouse.',0,4,)
    Q47 = st.slider('Q47. When I discuss with my spouse, I stay silent because I am afraid of not being able to control my anger. ',0,4,)
    Q48 = st.slider('Q48. I feel right in our discussions.',0,4,)
    Q49 = st.slider('Q49. I have nothing to do with what I have been accused of.',0,4,)
    Q50 = st.slider('Q50. I am not actually the one who is guilty about what I am accused of.',0,4,)
    Q51 = st.slider('Q51. I am not the one who is wrong about problems at home.',0,4,)
    Q52 = st.slider('Q52.  I wouldn not hesitate to tell my spouse about her/his inadequacy.',0,4,)
    Q53 = st.slider('Q53. When I discuss, I remind my spouse of her/his inadequacy.',0,4,)
    Q54 = st.slider('54. I am not afraid to tell my spouse about her/his incompetence.',0,4,)

    ok = st.button('Predict Divorce')
    if ok:
        x = np.array([[Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q40, Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q49, Q50, Q51, Q52, Q53, Q54]])
       
        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.001)
            my_bar.progress(percent_complete + 1)
        ans = model.predict(x)

        if ans[0] == 1:
            st.subheader('Possible chance of Divorce')
        elif ans[0] == 0:
            st.subheader('No chance of divorce enjoy')
        else:
            pass


        