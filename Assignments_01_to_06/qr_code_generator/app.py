import qrcode
import streamlit as st
import io
 
st.set_page_config(layout="wide")

st.title("QR code generator📇")
st.markdown("Welcome to QRcode generator ,generate your qrcode seamlessly")
st.divider()


col1,col2 = st.columns(2,gap="medium")

with col1:
  st.subheader("Enter specifications for your QRCode:")
  data=st.text_input("Enter data to encode: ")
  pattern=st.selectbox("Select pattern variant:",(1, 2, 3, 4 ,5))
  box=st.selectbox("Select box-size:",(5,10,15,20))
  pattern_color=st.text_input("Enter pattern color:").lower()
  box_color=st.text_input("Enter box color:").lower()
  
  qr= qrcode.QRCode( 
  version=pattern,
  box_size=box,
  border=4
 )
  if st.button("Generate:"):
   qr.add_data(data)
   qr.make(fit=True)
   image=qr.make_image(fill_color=pattern_color, back_color=box_color).convert("RGB")

   image_bytes=io.BytesIO()
   image.save(image_bytes,format="PNG")
   image_bytes.seek(0)


  with col2:
    st.image(image)
    st.download_button(
                label="Download QR Code",
                data=image_bytes,
                file_name="qr_code.png",
                mime="image/png"
            )