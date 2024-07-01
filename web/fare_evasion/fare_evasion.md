# Đề bài:

![Screenshot (649)](https://github.com/anhshidou/uiuctf-2024/assets/152991010/ec0c5344-7de1-45a2-8ee2-80ef19be7373)

# Giao diện ban đầu:
- Khi vào web ta sẽ có 1 giao diện như sau:

![Screenshot (650)](https://github.com/anhshidou/uiuctf-2024/assets/152991010/66f89fa0-85bb-4423-a090-cceb20106f5a)

- Khi ta bấm vào nút ```I'am a passenger``` thì 1 thông báo sẽ hiện ra:

![Screenshot (651)](https://github.com/anhshidou/uiuctf-2024/assets/152991010/5d687dec-e62d-431e-9505-59eb0e427930)

- Nhiệm vụ của bài này là ta phải leo lên quyền conductor, thử lục lọi xem có gì khác không
- Ở f12 ta có 1 đoạn suộc code nho nhỏ bên backend:
### Suộc:
```
<script>
    async function pay() {
      // i could not get sqlite to work on the frontend :(
      /*
        db.each(`SELECT * FROM keys WHERE kid = '${md5(headerKid)}'`, (err, row) => {
        ???????
       */
      const r = await fetch("/pay", { method: "POST" });
      const j = await r.json();
      document.getElementById("alert").classList.add("opacity-100");
      // todo: convert md5 to hex string instead of latin1??
      document.getElementById("alert").innerText = j["message"];
      setTimeout(() => { document.getElementById("alert").classList.remove("opacity-100") }, 5000);
    }
  </script>
```
- Dòng todo có vẻ là mấu chốt của bài này, nhưng mà ta cần tiếp tục tìm hiểu, ở trên ta có 1 cái secret, vậy dùng ở đâu?
- Tiếp theo ta có 1 đoạn jwt như sau:
### JWT:
```
eyJhbGciOiJIUzI1NiIsImtpZCI6InBhc3Nlbmdlcl9rZXkiLCJ0eXAiOiJKV1QifQ.eyJ0eXBlIjoicGFzc2VuZ2VyIn0.EqwTzKXS85U_CbNznSxBz8qA1mDZOs1JomTXSbsw0Zs
```
- Sau khi lên jwt.io, ta có thể suy đoán rằng secret sẽ nằm ở phần signature, lấy jwt đó thay vào cookie, ta thấy phần secret đằng sau đã biến mất, tuy nhiên đoạn mã đó khả năng cao hợp lệ, vậy tại sao lại như thế?
# Khai thác:
- Trước tiên, nhìn vào suộc ta cùng với dòng todo, ta sẽ hiểu được cách thức mà con web này hoạt động:
    - Sau khi nhận mã jwt, hệ thống sẽ kiểm tra signature xem có hợp lệ không, nếu hợp lệ sẽ lấy phần kid, sau đó md5 nó và tìm chuỗi md5 raw trong database xem nó có trùng với mã raw md5 đã được lưu không, nếu có, nó sẽ thực hiện truy vấn cột đó, nếu không thì nó sẽ không trả về kết quả
    - Đó chính là lý do tại sao passenger-key lại trả về kết quả, lý do đơn giản bởi vì giá trị đó có tồn tại trong database
    - Nhiệm vụ của chúng ta là phải lấy được dữ liệu của conductor để xử lý
- Về lỗ hổng, nhờ được hint https://cvk.posthaven.com/sql-injection-with-raw-md5-hashes mà mình mới có thể nghĩ ra được cách làm
- Thông qua link kia, ta thấy được là chúng ta có thể lợi dụng dạng raw của md5 để thực hiện sql injection
### Key:
 - kid="129581926211651571912466741651878684928"
### Leak database:
 - Sau khi thay key trên vào rồi cóp đoạn mã jwt đó vào, ta đã được server leak ra data cần thiết:

![Screenshot (646)](https://github.com/anhshidou/uiuctf-2024/assets/152991010/08c1b8b7-7f54-4443-a725-c01615639730)

- Có vẻ con server này sẽ check signature, nếu là của conductor thì cho flag
- Còn lại thì việc nhẹ lương cao, thay signature thành của conductor, và ta có:

![Screenshot (645)](https://github.com/anhshidou/uiuctf-2024/assets/152991010/3c4158ac-d3c2-41a8-86d7-64e98f326788)

GG

# Flag:
uiuctf{sigpwny_does_not_condone_turnstile_hopping!}
