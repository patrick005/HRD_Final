// script.js: 이미지 업로드 및 서버 전송 로직

let uploadedImages = [];

window.onload = () => {
  // 5초 후 splash 화면 제거
  setTimeout(() => {
    document.getElementById("splash").style.display = "none";
    document.getElementById("main").style.display = "block";
  }, 5000);
};

// 사용자가 이미지 선택 후 미리보기 표시 + 삭제 버튼 생성
function uploadImages() {
  const input = document.getElementById("fileInput");
  const files = input.files;

  for (const file of files) {
    const reader = new FileReader();
    reader.onloadend = () => {
      const imgData = reader.result;
      uploadedImages.push(imgData);

      const img = document.createElement("img");
      img.src = imgData;
      img.className = "preview";

      const delBtn = document.createElement("button");
      delBtn.innerText = "취소";
      delBtn.onclick = () => {
        img.remove();
        delBtn.remove();
        uploadedImages = uploadedImages.filter(i => i !== imgData);
      };

      const list = document.getElementById("imageList");
      list.appendChild(img);
      list.appendChild(delBtn);
    };
    reader.readAsDataURL(file);
  }
}

// 서버로 첫 번째 이미지를 전송
async function sendToServer() {
  if (uploadedImages.length === 0) {
    alert("전송할 이미지가 없습니다.");
    return;
  }

  const base64 = uploadedImages[0].split(',')[1];

  // TODO: <server_ip>는 플라스크 서버 ip로 변경
  // const response = await fetch("http://<SERVER_IP>:5000/api/v1/_secure_predict_xyz123", {
  const response = await fetch("http://192.168.0.100:5000/api/v1/_secure_predict_xyz123", {

    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      image_base64: base64,
      metadata: {
        user_id: "testuser",
        timestamp: new Date().toISOString()
      }
    })
  });

  const data = await response.json();
  document.getElementById("responseOutput").textContent = JSON.stringify(data, null, 2);
}
