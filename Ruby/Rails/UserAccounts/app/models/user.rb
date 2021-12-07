# email:string 
# password_digest:string
# ruby has built in email regex validation 
class User < ApplicationRecord
    has_secure_password 
    validates :email, presence: true, format: { with: /\A[^@\s]+@[^@\s]+\z/, message: "invalid email address" }
end