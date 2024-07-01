# Hip with the Youth

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/404d9443-d4fa-411b-b597-2ccd83725411)

## Analyzing

- While reading the challenge, I found some keywords such as **Long Island Subway Authority (LISA)**, **social media** and **instagram**

- Using Instagram as an evidence, I go to instagram then found Long Island Subway Authority. After that will be the rest

## Solution

- Go to instagram:

https://www.instagram.com/longislandsubwayauthority/

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/0d20f7ae-eb95-408e-9b30-2a3a42003c8c)

- Found a thread account, go to that thread account: https://www.threads.net/@longislandsubwayauthority?xmt=AQGzXwdAY8VaxzIvzwW644C0-8feGPQHS772DKZgZSfOkIk

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/b0011156-53e8-4632-b281-30a9f5dfce4b)

- Found the flag: **uiuctf{7W1773r_K!113r_321879}**

# An Unlikely Partnership

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/942ee4e6-5e34-4797-a37e-d7092cfb6489)

## Analyzing

- In this part, I'm going to search "long island subway authority" on google search.

## Solution

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/98212033-e20d-42ce-ae5c-a9d6ed08e647)

- After using the way in the analyze part, I found this one looked special 

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/3dfb1e80-8aff-4f52-867b-251489652146)

- It returns as I thought

**Flag: uiuctf{0M160D_U1UCCH4N_15_MY_F4V0r173_129301}**

# The weakest link

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/4e79e7e7-84af-4f00-8367-1e7ec2c9e6d3)

## Analyzing

- We can found some keywords from the challenge description: **Spotify collaboration**, **neither of them have the opsec to keep it private**
  
- From the part 2 of this series, I found looking at UIUC-chan linkedin Profile will have me a lot.

## Solution

- We need to analyze UIUC chan linkedin profile, if we do it, we will found one spotify link

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/b589cf00-5f63-44c5-9c14-9a70237e851c)

- Since we found it, we could actually see the collab or a "friend activity"

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/eb72aa27-cfeb-448c-a51a-c74d6bbcc9b8)

- After doing that, we will found it had a playlist called "song for train lovers"

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/4c592cd9-d044-4ea6-abe4-9885cb09a63c)

- After that, we can take the flag

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/b3a22a15-b052-4801-80d2-73de1bc8d499)

**Flag: uiuctf{7rU1Y_50N65_0F_7H3_5UMM3r_432013}**

# Night

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/0aa583c8-01a3-478b-af1b-0041dc21861a)


## Analyzing

- Now we are straight into geoguesser. We need to analyze the image

![chal](https://github.com/anhshidou/uiuctf-2024/assets/120787381/17626a84-02dd-4f30-85ab-0f02a5e277d7)

- In this image, we can find a tall building. Take it as a key point to find then using the google lens

- Next step, we know that the photo taken from road is on the right on the road. Then we found out that the author have been blurred out something, it might be front face of that tall building.

## Solution

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/91aa6c3f-4d6c-4b46-8c4c-a7d0e7fcbf05)

- I found the building named prudential so that the rest of challenge would be a lot easier

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/a04004de-f0e8-430e-b10e-c133950df823)

- Since the building named prudential wrote prudential on the opposite way of my among picture. I took it as a clue.

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/708d0b04-c3bc-46fe-b17b-f946a57a57ea)

- I found this road seems familliar, seems like the answer is here

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/6139fcc5-d3b4-4066-a163-43543b746467)

**Flag: uiuctf{Arlington Street, Boston**

# Chunky boi

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/a455a135-aace-44ef-b1bb-df69be465d15)

## Analyzing

![chal (2)](https://github.com/anhshidou/uiuctf-2024/assets/120787381/23ec880b-e2c5-475c-952e-99ecb7f841ff)

- We need to analyze the picture above.

- From the picture, we can know something: There is an aircraft looks like a military one, two aircraft from Alaska Airways.

- From the metadata, we found that seems like it was took on May 11st, 2024.

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/af9dc9ae-a01e-4013-a373-925c39dc2a1e)

- I took the military one as a key point. I found that the plane is Boeing C-17A Globemaster III with the registration is 07-7182

- Then find the flight schedule of the aircraft is my final move

## Solution

- After analyze it that much, I found a website that can track plane: https://radar.planespotters.net/?icao=ae20c3&lat=47.182&lon=-122.524&zoom=7.0&showTrace=2024-05-11

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/7c226368-051d-45ae-a0f3-0d8f62298df1)

- I found it going to Seattle, in Seattle there is only one airport that can handle this much aircraft is Seatac

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/723f9f7d-bd83-45c9-a340-be6079054142)

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/5123ad46-e877-4f93-ad85-bca64a2b1dc0)

- After these two images, my thought is totally cleared.

**Flag: uiuctf{Boeing C-17 Globemaster III, 47.462, -122.303}**

# New Dallas

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/edfcfdec-8a86-4cef-85e9-4b8ac65390e2)

## Analyzing

![chal (1)](https://github.com/anhshidou/uiuctf-2024/assets/120787381/8ef4965d-89a4-4e56-94f5-b2b761a58d2b)

- We found this image have a lot of details.

- First: There is a high-speed train and the railway

- Second: It on a city

- Third: It has a sign right after the railway

- Fourth: The train has green line stripe.

- By knowing all of this, I can reduce the range of my thought down to a metro line. It really helped me a lot.

# Solution

- There are a lot of metro line in China, I use this website to find the things I need: https://www.travelchinaguide.com/

- Then I found that the green line stripe is not for decoration, it also for Identification color of each metro line.

- Using chatgpt will help you create a list of metro line that has green identification color

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/4adfeae1-451a-45bb-bdd5-2ab5f7d812ed)

- After tested and searching for each metro line in the chatgpt list, I found a metro line that is suprisingly similar to the image is **Wuxi Metro Line 2**

- By using **https://www.travelchinaguide.com/cityguides/jiangsu/wuxi/subway/line2.htm** I can find the station and timetable so that I can take the exactly station to find it more accurately

- The nearest answer will be in Dongting Neighbourhood since it is very large which is suitable for 6-lane road

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/654dceee-1cf0-4523-84fa-1d5fc23fa9e6)

- We find the metro line and the train that completely correct. And the flag format is coordinates of intersection so that we need to find the intersection

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/1293df1d-f1a1-4772-a9fb-db8237ca2cf3)

- I found the intersection on the road next to the road of the metro line. Since the correct coord must be between the intersection, we will take the building with the coord of 31.579, 120.388

![image](https://github.com/anhshidou/uiuctf-2024/assets/120787381/8b13f990-d58c-4760-b30f-3604a18a89db)

**Flag: uiuctf{31.579, 120.388}**







